let register_button = document.querySelector('.register');

if (register_button) {
 register_button.addEventListener('click',
     (event) => window.location.href = 'register/');
}

 let login_button = document.querySelector('.login');

 if (login_button) {
  login_button.addEventListener('click',
      (event) => window.location.href = 'login/');
 }

 let main_button = document.querySelector('.main');

 if (main_button) {
  main_button.addEventListener('click',
      () => window.location.href = '/');
  main_button.addEventListener('click',
     (event) => console.log(event.currentTarget.innerHTML));
 }

 let test_button = document.querySelector('.test-button');

 if (test_button) {
  test_button.addEventListener('click',
      (event) => window.location.href = '/tests/list/');
 }

  let logout_button = document.querySelector('.logout');

 if (logout_button) {
  logout_button.addEventListener('click',
     () => window.location.href = '/logout/');
 }

 // select_test = document.querySelector('.select-test');
 //
 // if (select_test) {
 //  select_test.addEventListener('click',
 //      () => window.location.href = '/tests/questions/');
 // }
