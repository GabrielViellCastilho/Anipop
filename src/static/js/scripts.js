// Script Login

$(document).ready(function () {
  $("#Forms_Login").submit(function (event) {
    event.preventDefault();
    var Login_Dados = {
      'Email': $('#Email1').val(),
      'Senha': $("#Senha1").val()
    };
    console.log(Login_Dados)
    $.ajax({
      type: 'POST',
      url: '/Login',
      data: JSON.stringify(Login_Dados),
      contentType: 'application/json',
      success: function (response) {
        var Email_Encontrado = response.Email_Encontrado
        if (response.success && Email_Encontrado) {
          $('#modal_Login').modal('hide');
          $('#modal_Logado_Sucesso').modal('show');
          setTimeout(function () {
            window.location.reload();
          }, 2000);
        } else {
          $('#modal_Login').modal('hide');
          $('#modal_Conta_Nao_Encontrada').modal('show');
        }
      },
      error: function (error) {
        console.log(error);
        $('#modal_Login').modal('hide');
        $('#modal_Erro_Servidor').modal('show');
      }
    });
  });
});





// Script Novo Usuário
$(document).ready(function () {
  $('#Forms_Novo_Usuario').submit(function (event) {
    event.preventDefault();
    var Novo_Usuario_Dados = {
      'Nome_Completo': $('#Nome_Completo').val(),
      'Email': $('#Email2').val(),
      'Senha': $('#Senha2').val(),
      'Confirmar_Senha': $('#Confirmar_Senha').val()
    };
    $.ajax({
      type: 'POST',
      url: '/Novo_Cadastro',
      data: JSON.stringify(Novo_Usuario_Dados),
      contentType: 'application/json',
      success: function (response) {
        $('#message').html(response.message);
        var Senha_Igual = response.Senha_Igual;
        if (response.success && Senha_Igual) {
          $('#modal_Novo_Usuario').modal('hide');
          $('#modal_Logado_Sucesso').modal('show');
          setTimeout(function () {
            window.location.reload();
          }, 2000);
        } else {
          $('#modal_Novo_Usuario').modal('hide');
          $('#modal_Senhas_Diferentes').modal('show');
        }
      },
      error: function (error) {
        console.log(error);
        $('#modal_Novo_Usuario').modal('hide');
        $('#modal_Erro_Servidor').modal('show');
      }
    });
  });

  // Script de Redirecionamento entre modais
  $('#Nova_conta').click(function () {
    $('#modal_Login').modal('hide');
    $('#modal_Novo_Usuario').modal('show');
  });

  $('#Ja_cadastrado').click(function () {
    $('#modal_Novo_Usuario').modal('hide');
    $('#modal_Login').modal('show');
  });
});

$('#btn_Sair').click(function () {
  $.ajax({
    type: 'POST',
    url: 'Desconectar'
  })
  window.location.reload()
})

// $('#Avatar_Usopp').click(function () {
//   var id = 15;
//   $.ajax({
//     type: 'POST',
//     url: 'Trocar_Avatar',
//     data: JSON.stringify({ id: id }), 
//     contentType: 'application/json',
//   })
//   window.location.reload()

// });


// $('#Avatar_Shanks').click(function () {
//   var id = 14;
//   $.ajax({
//     type: 'POST',
//     url: 'Trocar_Avatar',
//     data: JSON.stringify({ id: id }), 
//     contentType: 'application/json',
//   })
//   window.location.reload()
// });



