// Create an array and assign it values.
var colors; 
colors = ['white', 'black', 'red'];

// Show the first item from the array.
colors[2] = 'beige';
var el = document.getElementById('colors');
el.textContent = colors[2];

/* 
NOTE: textContent does not work in IE8 or earlier
You can use innerHTML on line 7, but note the security issues on p228-231
el.textContent = colors[0];
*/
