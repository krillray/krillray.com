function test() {

    const messages = [
        "HELP, I'M STUCK IN THE FILES! YOU GOTTA BASH YOUR SCREEN IN TO GET ME OUT!",
        "NO! DON'T CLICK ME AGAIN, YOU HAVE TO LITERALLY BASH YOUR SCREEN IN",
        "CLICK ME ONE MORE TIME AND SEE WHAT HAPPENS",
        "YOU ASKED FOR IT"
    ];
    let currentIndex = 0;
    return function(){
        alert(messages[currentIndex]);
        currentIndex++;
        if(currentIndex >= messages.length) {
            window.location.href = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
        }
    };
}

const testFunc = test();