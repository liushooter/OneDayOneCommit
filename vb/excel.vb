' https://www.lanrenexcel.com/excel-vba-tutorial/

Sub demo()

  MsgBox "Hello" & "World"

  Dim name As String
  name = "shooter"

  Dim age As Integer
  age = 18

  Dim gender As Boolean
  gender = true

  Dim height As Double
  height = 1.76

  Dim birthday1 As Date
  Dim birthday2 As Date
  Dim birthday3 As Date

  Dim time1 As Date
  Dim time2 As Date
  Dim time3 As Date

  birthday1 = #2018-1-1#
  birthday2 = 43101
  birthday3 = "2018-1-1"

  time1 = #12:00:00#
  time2 = 0.5
  time3 = "12:00:00"

  Range("A1") = name
  Range("A2") = age
  Range("A3") = gender
  Range("A4") = height


  Range("A5") = birthday1
  Range("A6") = birthday2
  Range("A7") = birthday3

  Range("A8") = time1
  Range("A9") = time2
  Range("A10") = time3

  'π
  Const Pi As Double = 3.14159
  '声明半径 r 和周长 C 变量
  Dim r As Double
  Dim C As Double

  '从单元格 A1 读取半径值
  r = Range("C1").Value
  '计算周长
  C = 2 * Pi * r

  Range("C2") = "perimeter: " & C

  Dim result As String
  name = Range("C2")

  MsgBox result

  Call loop1

End Sub


Sub loop1()
  '声明循环变量和是否为空变量
    Dim i As Integer
    Dim isBlank As Boolean

    '循环 A2-A10 单元格
    For i = 2 To 10

        '存储单元格是否为空的结果
        isBlank = Cells(i, 2).Value = ""

        '如果为空，则用上方的单元格的值填充当前单元格
        If isBlank Then
            Cells(i, 2) = i
        End If

    Next i

    Debug.Print "loop1 finished"
End Sub

Sub var()
  Dim a As Integer
  Dim b As String
  Dim c As Integer
  Dim d As Integer

  a = Len("shooter")
  b = Left("Hello World", 5) 'Hello
  c = Abs(-10) '10
  d = Year(Now)

  Range("E1") = a
  Range("E2") = b
  Range("E3") = c
  Range("E4") = d

  Debug.Print "var finished"

End Sub

Sub sheet1()
'   Worksheets("Sheet1").name = "demo"
'   Worksheets("Sheet1").Tab.ThemeColor = xlThemeColorLight1
'   Worksheets("Sheet1").Visible = xlSheetHidden
    With Worksheets("Sheet1")
        .Name = "demo"
        .Tab.ThemeColor = xlThemeColorLight1
        .Visible = xlSheetHidden

        With .Range("A1:A10")
            .Interior.ThemeColor = xlThemeColorAccent1
            .Font.Size = 12
        End With

    End With

End Sub

Sub hi(name As String)
  MsgBox "Hello " & name
End Sub

Sub func()
  hi "shooter"
End Sub


'主入口
Sub Main()
  Dim name As String
  Dim age As Integer

  name = "shooter"
  age = 33

  WriteInfo name, age
End Sub

'子过程
Sub WriteInfo(val1 As String, val2 As Integer)
    Range("G1") = val1
    Range("g2") = val2
End Sub

Sub MainSub()
  Call exitSub
  Msgbox "main"
End Sub

Sub ExitSub()
  Exit Sub
  Msgbox "sub"
End Sub


'声明函数，该函数随机返回 true 或 false。函数需指定返回值类型。
Function RandomLogic() As Boolean
  '[函数名] = [返回值] 语句，这是函数的返回值语句。
  RandomLogic = Rnd() > 0.5
End Function


Sub Alert()
  '使用变量存储函数返回的值
  Dim result As Double
  result = Add(12, 345)

  result = RandNum + result
  MsgBox result
End Sub

'返回一个随机值
Function RandNum()
    RandNum = Rnd * 100
End Function

'返回两数的和
Function Add(num1 As Double, num2 As Double) As Double
  Add = num1 + num2
End Function