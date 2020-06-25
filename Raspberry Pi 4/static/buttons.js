window.onload =  () => {

    let left = new XMLHttpRequest();
    let right = new XMLHttpRequest();
    let forward = new XMLHttpRequest();
    let backward = new XMLHttpRequest();

    left.open("GET", 'http://127.0.0.1:5000/left', true);
    right.open("GET", 'http://127.0.0.1:5000/right', true);
    forward.open("GET", 'http://127.0.0.1:5000/forward', true);
    backward.open("GET", 'http://127.0.0.1:5000/backward', true);

    left.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    right.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    forward.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    backward.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    document.getElementById('leftBtn').addEventListener('click', () => {
         left.send();
    }) ;

    document.getElementById('rightBtn').addEventListener('click', () => {
         right.send();
    }) ;

    document.getElementById('forwardBtn').addEventListener('click', () => {
         forward.send();
    }) ;

    document.getElementById('backwardBtn').addEventListener('click', () => {
         backward.send();
    }) ;
};