    function formSwitch() {
        graph = document.getElementsByName('example')
        if (graph[0].checked) {
            // 好きな食べ物が選択されたら下記を実行します
            document.getElementById('red').style.display = "";
            document.getElementById('blue').style.display = "none";
        } else if (graph[1].checked) {
            // 好きな場所が選択されたら下記を実行します
            document.getElementById('red').style.display = "none";
            document.getElementById('blue').style.display = "";
        } else {
            document.getElementById('red').style.display = "none";
            document.getElementById('blue').style.display = "none";
        }
    window.addEventListener('load', formSwitch());
    }
