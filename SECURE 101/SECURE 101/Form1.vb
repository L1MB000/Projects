Imports System.Security.AccessControl
Imports System.IO
Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub FolderBrowserDialog1_HelpRequest(sender As Object, e As EventArgs) Handles FBD1.HelpRequest

    End Sub

    Private Sub btnBrowse_Click(sender As Object, e As EventArgs) Handles btnBrowse.Click
        With FBD1
            If .ShowDialog() = DialogResult.OK Then
                txtInp.Text = .SelectedPath
            End If
        End With
    End Sub

    Private Sub btnLock_Click(sender As Object, e As EventArgs) Handles btnLock.Click
        Dim fs As FileSystemSecurity = File.GetAccessControl(txtInp.Text)
        fs.AddAccessRule(New FileSystemAccessRule(Environment.UserName,
        FileSystemRights.FullControl, AccessControlType.Deny))
        File.SetAccessControl(txtInp.Text, fs)
        MessageBox.Show("Folder is now LOCKED!")

    End Sub

    Private Sub btnUnlock_Click(sender As Object, e As EventArgs) Handles btnUnlock.Click
        Dim fs As FileSystemSecurity = File.GetAccessControl(txtInp.Text)
        fs.RemoveAccessRule(New FileSystemAccessRule(Environment.UserName,
        FileSystemRights.FullControl, AccessControlType.Deny))
        File.SetAccessControl(txtInp.Text, fs)
        MessageBox.Show("Folder is now UNLOCKED!")

    End Sub

    Private Sub txtInp_TextChanged(sender As Object, e As EventArgs) Handles txtInp.TextChanged

    End Sub

    Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs)

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs)

    End Sub
End Class
