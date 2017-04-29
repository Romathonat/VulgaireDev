window.onload = function () {
    mathjaxNodes = document.getElementsByClassName("math-tex");

    for (i = 0; i < mathjaxNodes.length; i++) {
        parent = mathjaxNodes[i].parentNode;
        parent.className = parent.className + " centreur"
    }
}