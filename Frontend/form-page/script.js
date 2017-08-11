window.onload = function() {
    const WIDTH = 44;
    let nextInput = function() {
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

    let listenKeydown = function(e) {
        switch (e.keyCode) {
            case 39:
                nextInput()
                break;
            case 37:
                previousInput()
                break;
            case 9:
                e.preventDefault();
                nextInput();
                break;
            case 13:
                e.preventDefault();
                document.getElementsByClassName("form-body")[0].submit();
                break;
            default:

        }
        console.log(e);
    }

    let previousBtn = document.getElementsByClassName("previous")[0];
    let nextBtn = document.getElementsByClassName("next")[0];

    previousBtn.addEventListener('click', previousInput)
    nextBtn.addEventListener('click', nextInput)
    document.addEventListener("keydown", listenKeydown);
}
