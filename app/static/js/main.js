function toggleMenu() {

    const nav = document.querySelector("nav");

    if (!nav) {
        return;
    }

    if (nav.style.display === "flex") {

        nav.style.display = "none";

    } else {

        nav.style.display = "flex";
        nav.style.flexDirection = "column";
        nav.style.position = "absolute";
        nav.style.top = "75px";
        nav.style.left = "0";
        nav.style.right = "0";
        nav.style.background = "white";
        nav.style.padding = "20px";

    }
}