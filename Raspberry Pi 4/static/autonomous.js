window.onload =  () => {

    let start = new XMLHttpRequest();
    let stop = new XMLHttpRequest();

    start.open("GET", 'http://127.0.0.1:5000/start', true);
    stop.open("GET", 'http://127.0.0.1:5000/found', true);  // found is similar to stop


    start.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    stop.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    document.getElementById('startBtn').addEventListener('click', () => {
         start.send();
    }) ;

    document.getElementById('stopBtn').addEventListener('click', () => {
         stop.send();
    }) ;
};