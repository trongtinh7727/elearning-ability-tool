function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function getKey(question) {
    var tempKey = "";
    answer = item.getElementsByClassName('pbm');
    for (let a of answer) {
        tempKey = a.getElementsByTagName('span')[0].innerText
        check = a.getElementsByTagName('ins')[0].click()
    }

}

list = document.querySelector('#List-Question').children
for (let item of list) {
    question = item.getElementsByTagName('b');
    questionText = question[0].innerText
    answer = item.getElementsByClassName('pbm');
    for (let a of answer) {
        DA = a.getElementsByTagName('span')[0].innerText
        check = a.getElementsByTagName('ins')
        console.log(DA)
        console.log(check)
        if (DA == dict[questionText]) {
            check[0].click()
        }
        else{

        }
    }
    console.log('------------')
}

sleep(5)
document.querySelector('#btnNext').click()
