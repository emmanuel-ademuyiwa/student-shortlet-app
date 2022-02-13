if (document.getElementById('test').textContent === 'Available'){
    console.log(' available');
    document.getElementById('test').classList.remove('label-info');
    document.getElementById('test').classList.add('label-success');

}else{
    console.log('not available');
    document.getElementById('test').classList.remove('label-info');
    document.getElementById('test').classList.add('label-warning');

}


document.getElementById('del').addEventListener('click', function() {
    // add current score to the global score
    location.reload()
})