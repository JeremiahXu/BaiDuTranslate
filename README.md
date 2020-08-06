# BaiDuTranslate

**The demo test to access the Baidu Translate API. It use in python and javascript.**
*该演示测试访问百度翻译API。它使用 python和 javascript语言测试。*

1. 用**python**语言编写。

2. 用**h5+javesript+jQuery**语言编写。

```javascript
 $.ajax({
        url: 'http://api.fanyi.baidu.com/api/trans/vip/translate',
        type: 'get',
        dataType: 'jsonp',
        data: {
            q: query,
            appid: appid,
            salt: salt,
            from: from,
            to: to,
            sign: sign
        },
        success: function (data) {
            console.log(data);
        }
    });
```
