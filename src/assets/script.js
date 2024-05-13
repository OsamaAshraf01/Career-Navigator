var checks_count = 0;

function append_check(label_text) {
    checks_count += 1;
    // Creating the box
    const check = document.createElement("input");
    check.type = "checkbox";
    check.name = "check_{checks_count}";
    check.value = false;

    // Creating the label

    const label = document.createElement("label");
    label.for = check.name
    label.innerText = label_text;


    document.getElementById('check-boxes-div').appendChild(check);
    document.getElementById('check-boxes-div').appendChild(label);


};


function button_load() {
    // To make loading button
}