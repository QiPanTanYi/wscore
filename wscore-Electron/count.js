// 倒计时秒数
var seconds = 4;
// 获取倒计时元素
var countElement = document.getElementById("count");

// 更新倒计时函数
function updateCountdown() {
countElement.textContent = seconds;

if (seconds <= 0) {
    clearInterval(countdown);

    // 自动打开链接
    var searchLink = document.getElementById("search-link");
    window.open(searchLink.href, "_self");

    // 在当前页面中打开链接
    //window.location.href = searchLink.href;
}

seconds--;
}

// 更新倒计时初始状态
updateCountdown();

// 计时器
var countdown = setInterval(updateCountdown, 1000);