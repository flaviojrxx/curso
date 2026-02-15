
Projeto: Simulação de Ataques de Força Bruta com Medusa e Kali Linux
Este projeto demonstra a execução de auditorias de segurança focadas em ataques de força bruta (Brute Force) e Password Spraying. O objetivo é validar a robustez de credenciais em serviços comuns (FTP, SMB e HTTP) utilizando a ferramenta Medusa em um ambiente controlado e seguro.

1. Configuração do Ambiente
O laboratório foi estruturado utilizando virtualização para garantir o isolamento do tráfego:

Sistema Atacante: Kali Linux.

Sistema Alvo: Metasploitable 2 (contendo serviços vulneráveis e a aplicação DVWA).

Rede: Configurada em modo Host-Only no VirtualBox para permitir a comunicação exclusiva entre as máquinas virtuais.

2. Metodologia de Ataque
A. Brute Force no Serviço FTP
O ataque foi direcionado ao protocolo FTP para identificar credenciais de acesso de um usuário específico utilizando uma wordlist de senhas comuns.

Comando: medusa -h [IP_ALVO] -u msfadmin -P /usr/share/wordlists/rockyou.txt -M ftp

B. Password Spraying no SMB
Execução de técnica de Password Spraying, onde uma única senha é testada contra uma lista de múltiplos usuários. Esta técnica visa contornar políticas de bloqueio de conta que seriam ativadas por múltiplas tentativas em um único usuário.

Comando: medusa -h [IP_ALVO] -U lista_usuarios.txt -p Password123 -M smbnt

C. Automação de Tentativas em Formulário Web (DVWA)
Simulação de ataque de força bruta contra a interface de login da aplicação Damn Vulnerable Web Application (DVWA), explorando a falta de mecanismos de rate limiting no nível de aplicação.

Comando: medusa -h [IP_ALVO] -u admin -P wordlist.txt -M http -m DIR:/dvwa/login.php

3. Recomendações de Segurança e Mitigação
Com base nos ataques realizados, as seguintes medidas de defesa são recomendadas para fortalecer o ambiente:

Políticas de Senha: Implementação de requisitos mínimos de complexidade, tamanho e rotação periódica.

Account Lockout: Configuração de bloqueio temporário após um número definido de tentativas falhas de login.

Autenticação Multifator (MFA): Adição de uma camada extra de segurança que invalida a eficácia de senhas obtidas por força bruta.

Monitoramento e IPS: Utilização de sistemas de detecção e prevenção de intrusão (como Fail2Ban) para identificar e banir IPs que realizam múltiplas tentativas de conexão.

Ferramentas Utilizadas
Kali Linux: Plataforma de testes de intrusão.

Medusa: Ferramenta modular de força bruta paralela.

Metasploitable 2: Máquina virtual vulnerável para fins educacionais.
