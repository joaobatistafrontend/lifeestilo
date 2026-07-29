<?php
// Define o e-mail de destino (substitua pelo seu e-mail do plano Essentials da HostGator)
$para = "atendimento@lifeestetica.com.br";
$assunto = "Novo Agendamento pelo Site - Life Estética";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = isset($_POST["nome"]) ? strip_tags(trim($_POST["nome"])) : "";
    $email = isset($_POST["email"]) ? filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL) : "";
    $data = isset($_POST["data"]) ? strip_tags(trim($_POST["data"])) : "";
    $voucher = isset($_POST["voucher"]) ? strip_tags(trim($_POST["voucher"])) : "";
    $telefone = isset($_POST["telefone"]) ? strip_tags(trim($_POST["telefone"])) : "";
    $observacao = isset($_POST["observacao"]) ? strip_tags(trim($_POST["observacao"])) : "";

    if (empty($nome) || empty($email) || empty($telefone)) {
        http_response_code(400);
        echo json_encode(["status" => "error", "message" => "Por favor, preencha os campos obrigatórios (Nome, E-mail e Telefone)."]);
        exit;
    }

    // Monta a mensagem formatada do e-mail
    $conteudo = "Você recebeu uma nova solicitação de agendamento pelo site:\n\n";
    $conteudo .= "--------------------------------------------------------\n";
    $conteudo .= "Nome Completo: " . $nome . "\n";
    $conteudo .= "E-mail: " . $email . "\n";
    $conteudo .= "Telefone: " . $telefone . "\n";
    $conteudo .= "Data Solicitada: " . $data . "\n";
    $conteudo .= "Procedimento: " . $voucher . "\n";
    $conteudo .= "Observações: " . $observacao . "\n";
    $conteudo .= "--------------------------------------------------------\n";
    $conteudo .= "Data/Hora do envio: " . date("d/m/Y H:i:s") . "\n";

    // Cabeçalhos para o envio seguro no servidor cPanel/HostGator
    $remetente = "atendimento@lifeestetica.com.br";
    $headers = "From: Life Estética <" . $remetente . ">\r\n";
    $headers .= "Reply-To: " . $email . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();

    // Envia o e-mail usando a função mail() com a flag -f exigida pela HostGator
    if (mail($para, $assunto, $conteudo, $headers, "-f " . $remetente)) {
        echo json_encode(["status" => "success", "message" => "Solicitação de agendamento enviada com sucesso! Entraremos em contato em breve."]);
    } else {
        http_response_code(500);
        echo json_encode(["status" => "error", "message" => "Falha ao enviar o e-mail. Por favor, entre em contato via WhatsApp."]);
    }
} else {
    http_response_code(403);
    echo "Acesso proibido.";
}
?>
