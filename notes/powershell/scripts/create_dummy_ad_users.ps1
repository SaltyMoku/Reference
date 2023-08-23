$user_number = 20

while ($userNumber -gt 0 ){
    $new_user = ''
    [System.Collections.Arraylist]$tmp = "Ra","nd","om","Us","er"," "
    while ($tmp.Count -ne 0){
        $rand = Get-Random -min 0 -max ($tmp.Count)
        $new_user = $new_user + $tmp[$rand]
        $tmp.Remove($rand)
    }
    echo $new_user
    New-AdUser $new_user -AccountPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force)
    $user_number--
}