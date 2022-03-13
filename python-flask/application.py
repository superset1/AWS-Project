from flask import Flask

# print a nice greeting.
def wtf(username="man"):
    return '''
    <h1>What happened %s???!</h1>
    <h2>Where are u going???!</h2>
    ''' % username

# some bits of text for the page.
header_text = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta property="og:title" content="Road to DevOps"/>
    <meta property="og:description" content="This is a Python application in a Docker container on AWS"/>
    <meta property="og:site_name" content="Road to DevOps"/>
    <meta property="og:image" content="https://www.roadtodevops.ru/static/img/Devops1.png"/>
    <meta property="og:type" content="website" />
    <meta property="og:updated_time" content="1440432930" />
    <title>This is a Python application in a Docker container on AWS</title>

    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-D4L0M2XZYR"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-D4L0M2XZYR');
    </script>
    <!-- Global site tag (gtag.js) - Google Analytics -->

    <!-- Yandex.Metrika counter -->
    <script type="text/javascript" >
        (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
        (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");
    
        ym(87690720, "init", {
            clickmap:true,
            trackLinks:true,
            accurateTrackBounce:true,
            webvisor:true
        });
    </script>
    <noscript><div><img src="https://mc.yandex.ru/watch/87690720" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
    <!-- /Yandex.Metrika counter -->

    <link rel="stylesheet" href="static/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Lobster+Two&display=swap" rel="stylesheet">
    <link rel="icon" href="static/img/favicon.ico" type="image/ico" >
</head>
    <body class="python">
    '''
instructions = '''
        <h1>This app was made in Python,</h1>
        <h2>carefully packaged in a Docker container</h2>
        <h3>and deployed to AWS!</h3>
    '''
home_link = '<h3><a href="/">Back</a></h3>\n'
footer_text = '''
        <div>
            <img src="static/img/Devops1.png" width="30%" alt="Ups...">
            <img src="static/img/Moby-logo.png" width="30%" alt="Ups...">
            <img src="static/img/Amazon_Web_Services_logo_AWS.png" width="30%" alt="Ups..."> 
            <hr color="gray">
        <div>
        </body>\n</html>
        '''

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', '<h1>WTF???! Where are u going???</h1>', (lambda username:
    header_text + wtf('bro') + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0')