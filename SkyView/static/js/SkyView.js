const weatherMain = "{{ weather.main|default:'' }}";

const body = document.body;

if(weatherMain.includes('Rain')){
    body.className = 'rainy';
}

else if(weatherMain.includes('Cloud')){
    body.className = 'cloudy';
}

else{
    body.className = 'sunny';
}