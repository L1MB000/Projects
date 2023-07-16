<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Me.txtInp = New System.Windows.Forms.TextBox()
        Me.lblInp = New System.Windows.Forms.Label()
        Me.btnBrowse = New System.Windows.Forms.Button()
        Me.btnLock = New System.Windows.Forms.Button()
        Me.btnUnlock = New System.Windows.Forms.Button()
        Me.FBD1 = New System.Windows.Forms.FolderBrowserDialog()
        Me.SuspendLayout()
        '
        'txtInp
        '
        Me.txtInp.Location = New System.Drawing.Point(137, 170)
        Me.txtInp.Name = "txtInp"
        Me.txtInp.Size = New System.Drawing.Size(485, 26)
        Me.txtInp.TabIndex = 0
        '
        'lblInp
        '
        Me.lblInp.AutoSize = True
        Me.lblInp.Location = New System.Drawing.Point(133, 113)
        Me.lblInp.Name = "lblInp"
        Me.lblInp.Size = New System.Drawing.Size(84, 20)
        Me.lblInp.TabIndex = 1
        Me.lblInp.Text = "File Name:"
        '
        'btnBrowse
        '
        Me.btnBrowse.Location = New System.Drawing.Point(137, 238)
        Me.btnBrowse.Name = "btnBrowse"
        Me.btnBrowse.Size = New System.Drawing.Size(80, 41)
        Me.btnBrowse.TabIndex = 2
        Me.btnBrowse.Text = "Browse"
        Me.btnBrowse.UseVisualStyleBackColor = True
        '
        'btnLock
        '
        Me.btnLock.Location = New System.Drawing.Point(335, 238)
        Me.btnLock.Name = "btnLock"
        Me.btnLock.Size = New System.Drawing.Size(82, 41)
        Me.btnLock.TabIndex = 3
        Me.btnLock.Text = "Lock"
        Me.btnLock.UseVisualStyleBackColor = True
        '
        'btnUnlock
        '
        Me.btnUnlock.Location = New System.Drawing.Point(547, 238)
        Me.btnUnlock.Name = "btnUnlock"
        Me.btnUnlock.Size = New System.Drawing.Size(75, 41)
        Me.btnUnlock.TabIndex = 4
        Me.btnUnlock.Text = "Unlock"
        Me.btnUnlock.UseVisualStyleBackColor = True
        '
        'FBD1
        '
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(9.0!, 20.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(800, 450)
        Me.Controls.Add(Me.btnUnlock)
        Me.Controls.Add(Me.btnLock)
        Me.Controls.Add(Me.btnBrowse)
        Me.Controls.Add(Me.lblInp)
        Me.Controls.Add(Me.txtInp)
        Me.Name = "Form1"
        Me.Text = "Folder Lock/Unlock"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents txtInp As TextBox
    Friend WithEvents lblInp As Label
    Friend WithEvents btnBrowse As Button
    Friend WithEvents btnLock As Button
    Friend WithEvents btnUnlock As Button
    Friend WithEvents FBD1 As FolderBrowserDialog
End Class
