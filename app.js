const btnClicker = document.querySelector('.btn')
const bgColor = document.querySelector('#bg-color')
const btnAdd = document.querySelector('.btn')
const mainBlock = document.querySelector('.parent')
const content = document.getElementById('content')


let blocks = JSON.parse(localStorage.getItem('infoblock')) || []
renderBlocks()
btnAdd.addEventListener('click', function(){
    bebraBlock()
    var blocksInfo = {
        color: bgColor.value,
        text: content.value
    }
    blocks.push(blocksInfo)
    localStorage.setItem('infoblock', JSON.stringify(blocks))
    renderBlocks()

})


function renderBlocks(){
    mainBlock.innerHTML = ' '
    blocks.forEach(elem => {
        const div = document.createElement('div')
        div.classList.add('block')
        div.style.backgroundColor = elem.color
        div.textContent = elem.text
        mainBlock.append(div)
    })
}

function bebraBlock(){
    localStorage.getItem(JSON.stringify('infoblock'))
    blocks.forEach(elem => {
        backgroundColor = elem.bgColor
        textContent = elem.content
    })
}