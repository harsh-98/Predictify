window.onload = function() {
    let questions = document.getElementsByClassName("question-container");
    let firstQuestion = questions[0];
    if(firstQuestion)
        firstQuestion.style["display"] = "block";

    let prevQue = document.getElementsByClassName("left-navigate")[0];
    let nextQue = document.getElementsByClassName("right-navigate")[0];
    const totalQueLen = questions.length;
    let currentQuestionNo = 0;

    let nextQuestion = function(e) {
        currentQuestionNo++;
        if (currentQuestionNo < totalQueLen) {
            questions[currentQuestionNo - 1].style["display"] = "none";
            questions[currentQuestionNo].style["display"] = "block";
        }
        else {
            alert("kha ja rha hai mkl form submit kar")
            currentQuestionNo--;
        }
    }

    let prevQuestion = function(e) {
        currentQuestionNo--;
        if (currentQuestionNo >= 0) {
            questions[currentQuestionNo + 1].style["display"] = "none";
            questions[currentQuestionNo].style["display"] = "block";
        }
        else {
            alert("kha ja rha hai mkl form submit kar");
            currentQuestionNo++;
        }
    }

    let checkOption = function(e) {
        let question = questions[currentQuestionNo];
        let checkBox = e.target;
        let checked = question.getElementsByClassName("checked")[0];
        if(checked) {
            checked.className = "check-box";
            checked.innerHTML = "";
        }
        checkBox.className = "check-box checked";
        checkBox.innerHTML = "<div id='checked' class='selected-option'></div>"
    }

    let submitForm = function() {
        let checkedOptions = document.getElementsByClassName("checked");
        let formData = [];
        for (var i = 0; i < checkedOptions.length; i++) {
            formData.push(checkedOptions[i].dataset)
        }
        if(formData.length === totalQueLen)
            console.log("Form filled ", formData)
        else {
            alert("bhai form to bhar le")
        }
    }

    let allOptions = document.getElementsByClassName("check-box");
    for (var i = 0; i < allOptions.length; i++) {
        allOptions[i].addEventListener("click", checkOption);
    }
    prevQue.addEventListener("click", prevQuestion);
    nextQue.addEventListener("click", nextQuestion);

    let submitButton = document.getElementsByClassName("submit-button")[0];
    submitButton.addEventListener("click", submitForm)
}
