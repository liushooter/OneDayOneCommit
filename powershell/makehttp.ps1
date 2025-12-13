$headers=@{}
$headers.Add("accept", "application/json")
$headers.Add("content-type", "application/json")
$response = Invoke-WebRequest -Uri 'https://www.so.com/' -Method POST -Headers $headers
