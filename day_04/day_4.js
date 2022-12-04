const fileInput = document.getElementById("file_input")

fileInput.addEventListener("input", (e) => {
    const file = e.target.files[0]
    if (file) {
        const reader = new FileReader()
        reader.readAsText(file)
        reader.onload = () => {
            part_1(reader.result);
            part_2(reader.result);
        }
    }
})

function part_1(input) {
    let lines = input.split("\n");
    let erg = 0;
    for (let line in lines) {
        if (!lines[line]) break
        let arr = lines[line].match(/\d+/gm).map(number => parseInt(number, 10));
        if ((arr[0] <= arr[2] && arr[1] >= arr[3]) || (arr[0] >= arr[2] && arr[1] <= arr[3])) erg++;
    }
    console.log("the answer for part_1 is: " + erg);
}

function part_2(input) {
    let lines = input.split("\n");
    let erg = 0;
    for (let line in lines) {
        if (!lines[line]) break
        let arr = lines[line].match(/\d+/gm).map(number => parseInt(number, 10));
        if (arr[0] <= arr[3] && arr[1] >= arr[2]) erg++;
    }
    console.log("the answer for part_2 is: " + erg);
}
