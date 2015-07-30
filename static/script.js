$('img').on('dragstart', function(event) { event.preventDefault(); });

navigator.geolocation.getCurrentPosition(function(position) {
  console.log(position.coords.latitude, position.coords.longitude);
});