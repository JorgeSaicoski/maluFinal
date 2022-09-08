const menuIcon = document.getElementById('menuIcon')
const navBarFlex = document.getElementById("navFlex")
const itemNavFlex = document.getElementById("itemNavFlex")
const logoFlex = document.getElementById("logoFlex")


let isOpen = false

console.log("working")
const changeOpen =()=> {

    console.log("click")
    if (isOpen) {
      isOpen = false


      menuIcon.classList.remove("button-active")
      navBarFlex.classList.remove("header-active")
      itemNavFlex.classList.remove("header-navbar-active")



    }else{
      isOpen = true


      menuIcon.classList.add("button-active")
      navBarFlex.classList.add("header-active")
      itemNavFlex.classList.add("header-navbar-active")




    }
  }

/*Nav Bar clicks*/
logoFlex.addEventListener("click", function(e){
  console.log("click")
  changeOpen()
})
menuIcon.addEventListener("click", function(e){
  console.log("click")
  changeOpen()
})
console.log("end")
