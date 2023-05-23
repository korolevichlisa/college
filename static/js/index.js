window.addEventListener("load", () => {
  document.querySelector(".loader_bg").classList.add("disppear")
  
  let currentYearElement = document.querySelector('#current-year')

  if (currentYearElement) {
    currentYearElement.innerHTML = new Date().getFullYear()
  }
})