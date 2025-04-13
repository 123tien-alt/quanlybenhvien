// Lấy tất cả các liên kết trong thanh điều hướng
const navLinks = document.querySelectorAll('.nav-link');

// Lắng nghe sự kiện cuộn trang
window.addEventListener('scroll', () => {
    let currentSection = '';
    
    // Lặp qua tất cả các section để xác định section nào đang hiển thị trên màn hình
    document.querySelectorAll('section').forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;

        if (pageYOffset >= sectionTop - sectionHeight / 2) {
            currentSection = section.getAttribute('id');
        }
    });

    // Cập nhật class active cho các liên kết trong thanh điều hướng
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSection}`) {
            link.classList.add('active');
        }
    });
});

// Lắng nghe sự kiện click vào các liên kết trong thanh điều hướng
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetId);

        // Cuộn mượt mà đến phần nội dung tương ứng
        targetSection.scrollIntoView({ behavior: 'smooth' });
    });
});
// Hàm tìm kiếm cho bảng
function searchTable(tableId) {
  // Lấy giá trị từ ô input tìm kiếm
  const searchInput = document.getElementById('search-' + tableId).value.toLowerCase();
  // Lấy bảng mà ta cần tìm kiếm
  const table = document.getElementById(tableId + '-table');
  const rows = table.getElementsByTagName('tr');
  
  // Lặp qua từng hàng của bảng
  for (let i = 1; i < rows.length; i++) {  // Bỏ qua dòng tiêu đề (i = 1)
      const cells = rows[i].getElementsByTagName('td');
      let rowMatch = false;

      // Lặp qua các cột của mỗi hàng
      for (let j = 0; j < cells.length; j++) {
          const cell = cells[j];
          if (cell.innerText.toLowerCase().includes(searchInput)) {
              rowMatch = true;
              break; // Nếu tìm thấy từ khóa trong cột này thì không cần kiểm tra các cột còn lại
          }
      }

      // Hiển thị hoặc ẩn hàng dựa trên kết quả tìm kiếm
      if (rowMatch) {
          rows[i].style.display = ''; // Hiển thị hàng
      } else {
          rows[i].style.display = 'none'; // Ẩn hàng
      }
  }
}
