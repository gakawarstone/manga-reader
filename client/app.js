document.addEventListener('keydown', event => {
  if (event.code == 'ArrowRight' || event.code == 'ArrowLeft') {
    img = document.querySelector('img')
    img_src = img.getAttribute('src')
    img_number = img_src.slice(4, 7)

    if (event.code == 'ArrowRight') {
      img_number = Number(img_number) + 1
    }

    if (event.code == 'ArrowLeft') {
      img_number = Number(img_number) - 1
    }

    if (img_number > 18) {
      chapter_number = document.createElement('h3')
      chapter_number.innerHTML = 'Chapter 54'
      document.body.appendChild(chapter_number)
    } else {
      document.querySelectorAll('h3').forEach(element => {
        element.innerHTML = ''
      })
    }

    img.setAttribute(
      'src',
      `src/${
        '0'.repeat(3 - String(img_number).length) + String(img_number)
      }.png`
    )

    window.scrollTo(0, 0)
  }
})