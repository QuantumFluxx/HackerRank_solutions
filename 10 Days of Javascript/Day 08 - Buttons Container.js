CSS:

.btnClass {

    width: 96px;

    height: 48px;

    font-size: 24px;

}


JS:

var btn = document.createElement("Button");
btn.innerHTML = "0";
btn.id = "btn";
btn.className = "btnClass";
document.body.appendChild(btn);
btn.onclick = function() {
    btn.innerHTML+=2;
}


HTML:

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Button</title>
        <link rel="stylesheet" href="css/button.css" type="text/css">
    <style>
        .button {
            width: 96px;
            height: 48px;
            font-size: 24px;
        }
    </style>
    </head>
    <body>
        <script>
            var clickBtn = document.createElement('button');
            let counter = 0;
            clickBtn.innerHTML = counter;
            clickBtn.id = 'btn';
            clickBtn.className = 'button';
            document.body.appendChild(clickBtn);

            clickBtn.onclick = function () {
                counter++;
                btn.innerHTML = counter.toString();
            };
        </script>
    </body>
</html>