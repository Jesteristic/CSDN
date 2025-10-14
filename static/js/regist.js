$(function () {
    function bindCaptchaBtnClickEvent() {
        $("#btn_send_captcha").click(function (event) {
            let $this = $(this); // 获取当前点击的按钮
            let email = $("#email").val();
            if (!email) {
                alert("邮箱地址不能为空！！！");
                return;
            };
            //  取消按钮点击事件
            $this.off("click");
            // 发送ajax请求
            $.ajax({
                url: "/auth/send_captcha_email/?email="+email,
                method: "GET",
                data: { email: email },
                success: function (data) {
                    if (data.code === 200){alert("验证码发送成功，请注意查收！！！")}
                    else {alert(data.message)};
                    
                },
                fail: function () {
                    alert("验证码发送失败，请稍后重试！！！");
                }
            });
            // 计时器倒计时
            let countdown = 60;
            $this.text(countdown + "秒后重新获取");
            let timer = setInterval(function () {
                if (countdown <= 0) {
                    $this.text("获取验证码");
                    // 消除计时器
                    clearInterval(timer);
                    // 重新绑定点击事件
                    bindCaptchaBtnClickEvent();
                } else {
                    $this.text(countdown + "秒后重新获取");
                    countdown--;
                }
            }, 1000);
        })
    }
    bindCaptchaBtnClickEvent();
})