window.onload = function () {
    const { createEditor, createToolbar } = window.wangEditor

    const editorConfig = {
        placeholder: '请输入发布内容...',
        onChange(editor) {
            const html = editor.getHtml()
            console.log('editor content', html)
            // 也可以同步到 <textarea>
        },
    }

    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>',
        config: editorConfig,
        mode: 'default', // or 'simple'
    })

    const toolbarConfig = {}

    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // or 'simple'
    });

    $('#submit-btn').click(function(event){
        // 阻止按钮默认行为
        event.preventDefault();
        let title = $("input[id='title']").val();
        let category=$("#category-select").val();
        let content=editor.getHtml();
        let csrfmiddlewaretoken=$("input[name='csrfmiddlewaretoken']").val()
        $.ajax({
            url:'/blog/publish_blog',
            method:'POST',
            data:{
                title:title,
                category:category,
                content:content,
                csrfmiddlewaretoken:csrfmiddlewaretoken
            },
            success:function(result){
                if (result['code']==200){
                    // 跳转到博客详情页面
                    window.location='/blog/'+ result['data']['blog_id']
                }else{
                    alert(result['msg'])
                }
            },
            fail: function () {
                alert("系统异常，请重试！");
            }
            
        })
    });
};

