# Cài 1 lần (USER TỰ CHẠY): cho nút "📂 Mở thư mục" trên bảng HTML mở được File Explorer.
# Đăng ký giao thức aivideo-open: cho RIÊNG tài khoản Windows hiện tại (HKCU, không cần admin).
# Link chỉ mở / chọn file bằng explorer.exe, không chạy file (xem open-handler.ps1).
#   Cài:  powershell -ExecutionPolicy Bypass -File _tools\install-open-handler.ps1
#   Gỡ:   powershell -ExecutionPolicy Bypass -File _tools\install-open-handler.ps1 -Uninstall
param([switch]$Uninstall)
$key = "HKCU:\Software\Classes\aivideo-open"
if ($Uninstall) { Remove-Item -Recurse -Force $key -ErrorAction SilentlyContinue; "Đã gỡ aivideo-open."; exit 0 }
$handler = Join-Path $PSScriptRoot "open-handler.ps1"
New-Item -Force $key | Out-Null
Set-ItemProperty $key "(default)" "URL:AI Video open folder"
Set-ItemProperty $key "URL Protocol" ""
New-Item -Force "$key\shell\open\command" | Out-Null
Set-ItemProperty "$key\shell\open\command" "(default)" "powershell.exe -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$handler`" `"%1`""
"Đã cài. Nút '📂 Mở thư mục' trên bảng HTML giờ mở được File Explorer (lần đầu trình duyệt có thể hỏi cho phép → chọn Mở / Open)."
