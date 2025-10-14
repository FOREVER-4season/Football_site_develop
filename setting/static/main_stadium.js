// 슬라이더 딜레이 주기
let swiper = new Swiper(".mySwiper", {
                loop: true,
                autoplay: {delay: 3000, disableOnInteraction: false},
                speed: 800
            });


const days = ["일", "월", "화", "수", "목", "금", "토"];
const today = new Date();
today.setHours(0, 0, 0, 0);
let selectedDate = new Date(today);
let startDate = new Date(today);

// 7일 달력 만들기 디자인 요소도 가미

function renderCalendar(selected) {
    const calendarList = document.getElementById("calendarList");
    calendarList.innerHTML = "";

    for (let i = 0; i < 7; i++) {
        const date = new Date(startDate);
        date.setDate(startDate.getDate() + i);

        const li = document.createElement("li");
        li.style.cursor = "pointer";
        li.style.textAlign = "center";
        li.style.padding = "10px";
        li.style.width = "100px";
        li.style.listStyle = "none";

        li.innerHTML = `<div style="font-weight:bold;">${date.getDate()}</div><div>${days[date.getDay()]}</div>`;

        if (date.toDateString() === selected.toDateString()) {
            li.style.background = "#1a73e8";
            li.style.color = "white";
            li.style.borderRadius = "38px";
        }

        li.onclick = () => {
            selectedDate = date;
            renderCalendar(selectedDate);
            loadMatches(selectedDate);
        };

        calendarList.appendChild(li);
    }
}

// 이전버튼 함수

function prevDay() {
    if (selectedDate <= today) return;
    selectedDate.setDate(selectedDate.getDate() - 1);
    startDate = new Date(selectedDate);
    renderCalendar(selectedDate);
    loadMatches(selectedDate);
}

// 다음버튼 함수

function nextDay() {
    selectedDate.setDate(selectedDate.getDate() + 1);
    startDate = new Date(selectedDate);
    renderCalendar(selectedDate);
    loadMatches(selectedDate);
}

// ✅ 경기 불러오기 Ajax

function renderMatches(matches) {
    const container = document.getElementById("matchListContainer");
    if (matches.length === 0) {
        container.innerHTML = `<p class="text-center text-muted">해당 날짜에 경기가 없습니다.</p>`;
        return;
    }

    let html = `<ul class="list-group mx-auto">`;

    matches.forEach(match => {
        let statusHTML = "";
        if (match.status === "신청가능") {
            statusHTML = `<small class="text-success">신청가능</small>`;
        } else if (match.status === "마감임박") {
            statusHTML = `<small class="text-danger fw-bold">🔥 마감임박</small>`;
        } else {
            statusHTML = `<small class="text-secondary">마감</small>`;
        }

        html += `
                <li class="list-group-item d-flex justify-content-between align-items-center py-3 px-3 match-row" data-href="/stadium/${match.id}">
                    <div class="fw-bold text-center" style="width:140px;">
                        ${match.start_time}<br>${statusHTML}
                    </div>
                    <div class="flex-grow-1 px-2 text-start fw-bold">
                        ${match.stadium_name}
                    </div>
                    <div style="width:60px; text-align:center;">
                        ${match.status === "신청마감"
            ? `<span class="text-muted" style="font-size:20px; opacity:0.5;">🤍</span>`
            : isLoggedIn
                ? `<button class="btn btn-light btn-sm favorite-btn" data-id="${match.id}" style="font-size:20px;">🤍</button>`
                : `<a href="/auth/login" class="btn btn-light btn-sm" style="font-size:20px;">🤍</a>`
        }
                    </div>
                </li>`;
    });

    html += "</ul>";
    container.innerHTML = html;

    // 상세페이지 이동 이벤트 바인딩
    document.querySelectorAll(".match-row").forEach(row => {
        row.addEventListener("click", function (e) {
            if (!e.target.classList.contains("favorite-btn")) {
                window.location.href = this.dataset.href;
            }
        });
    });

    // 하트 버튼 클릭 이벤트 바인딩
    document.querySelectorAll(".favorite-btn").forEach(btn => {
        btn.addEventListener("click", function (e) {
            e.stopPropagation();
            if (!isLoggedIn) {
                alert("로그인이 필요합니다.");
                window.location.href = "/auth/login";
                return;
            }
            if (this.innerHTML === "🤍") {
                this.innerHTML = "❤️";
                fetch(`/matches/favorite/${this.dataset.id}`, {method: "POST"});
            } else {
                this.innerHTML = "🤍";
                fetch(`/matches/favorite/${this.dataset.id}`, {method: "DELETE"});
            }
        });
    });
}

// 날짜 객체를 불러와서 문자열로 바꾸되 하루 밀리는 현상 방지용

function formatDateLocal(date) {
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, "0");
    const day = date.getDate().toString().padStart(2, "0");
    return `${year}-${month}-${day}`;
}

// 실제 굴러가는 함수 정리


function loadMatches(date) {
    const dateStr = formatDateLocal(date);
    fetch(`/api/matches?date=${dateStr}`)
        .then(res => res.json())
        .then(renderMatches)
        .catch(err => console.error("경기 불러오기 실패:", err));
}

renderCalendar(selectedDate);
loadMatches(selectedDate);
