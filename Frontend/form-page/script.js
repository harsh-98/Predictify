window.onload = function() {
    const WIDTH = 44
    let nextInput = function(e) {
        let formBody = document.getElementsByClassName("form-body")[0];
        let maxOffset = document.getElementsByClassName("input-element").length * 44;
        let newOffset = parseInt(formBody.style.left? formBody.style.left: 0) - WIDTH;
        Math.abs(newOffset) < maxOffset?
            formBody.style.left = `${newOffset}rem`:
        alert("Nothing beyond this");
    }

    let previousInput = function() {
        let formBody = document.getElementsByClassName("form-body")[0];
        let maxOffset = document.getElementsByClassName("central-input").length * 44;
        let newOffset = parseInt(formBody.style.left? formBody.style.left: 0)  + WIDTH;
        newOffset <= 0?
            formBody.style.left = `${newOffset}rem`:
        alert("Nothing before this");
    }

    let previousBtn = document.getElementsByClassName("previous");
    for(let i = 0; i < previousBtn.length; i++)
        previousBtn[i].addEventListener('click', previousInput)
    let nextBtn = document.getElementsByClassName("next");
    for(let i = 0; i < nextBtn.length; i++)
        nextBtn[i].addEventListener('click', nextInput)
}
