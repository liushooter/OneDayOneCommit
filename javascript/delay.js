var delay = (function(){
  var timer = 0;
  return function(callback, ms){
    clearTimeout (timer);
    timer = setTimeout(callback, ms);
  };
})();

$('input').keyup(function() {
    delay(function(){
      alert('Time elapsed!');
    }, 1000 );
});


// http://stackoverflow.com/a/1909508/1240067