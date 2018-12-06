var level=1;

var progression = JSON.parse(document.getElementById('progression').innerHTML);
console.log(progression);

function level_up() {
    if ( level >= 10 ) {
        return;
    }
    ++level;
    console.log(progression[level]);
}
function level_down() {
    if ( level <= 1 ) {
        return;
    }
    --level;
    console.log(progression[level]);
}
