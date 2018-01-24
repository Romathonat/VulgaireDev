window.onload = function () {
    mathjaxNodes = document.getElementsByClassName("math-tex");

    for (i = 0; i < mathjaxNodes.length; i++) {
        parent = mathjaxNodes[i].parentNode;
        parent.className = parent.className + " centreur"
    }
    var aCodes = document.getElementsByTagName('pre');
    for (var i=0; i < aCodes.length; i++) {
         hljs.highlightBlock(aCodes[i]);
    }
}

