var progression = JSON.parse(document.getElementById('progression').innerHTML);

function change_level(event_obj) {
    level = event_obj.target.innerHTML;
    document.getElementById("hit_points").innerHTML = progression[level]['hit_points'] + " / " + progression[level]['hit_points'];
    document.getElementById("xp").innerHTML = progression[level]['xp'];
    document.getElementById("total_slots").innerHTML = progression[level]['attributes']['constitution'];
    document.getElementById("print_level").innerHTML = level;
    document.getElementById("level").innerHTML = "<u> " + level + " </u>";
    for ( var attribute in progression[level]['attributes'] ) {
        document.getElementById(attribute + "_defense").innerHTML =
            progression[level]['attributes'][attribute];
        document.getElementById(attribute + "_bonus").innerHTML =
            progression[level]['attributes'][attribute] - 10;
    }
    document.getElementById('dropdown_item').style.display="none";
}

function main() {
    document.addEventListener('DOMContentLoaded', function () {
      document.getElementById('dropdown_item')
              .addEventListener('click', change_level);
    });
    document.getElementById("level_dropdown").onmouseover = function() {
         document.getElementById('dropdown_item').style.display="block";
            };
    document.getElementById("level_dropdown").onmouseout  = function() {
         document.getElementById('dropdown_item').style.display="none";
            };
}

main()
