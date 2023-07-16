;ERICKO BAYU LISTYO SUHERMAN - TP062715

.model small
.stack 100h
.data
	stock_size equ 40
	; stock id, name, quantity, credit
	stock   dw 0,1,2,3,4,5,6,7,8,9
			db "Kevlar    ",  "Glock-19  ", "Holo sight", "9mm Ammo  ", "M1 Abrams ", "MP5       ", "Pindad-SS2", "F22 Raptor", "SAAB JAS39", "Anoa 6x6  "
			dw 90, 23, 38, 255, 3, 18, 8, 3, 6, 12, 10, 25, 15, 5, 250, 50, 85, 500, 350, 100, 1, 0, 1, 1, 2, 0, 1, 2, 0, 1, '$'	
	stock_id_offset dw 0
	stock_name_offset dw 20
	stock_quantity_offset dw 120
	stock_credit_offset dw 140	
    stock_sold dw 0,0,0,0,0,0,0,0,0,,'$' ; quantity sold 
    stock_credit dw 10, 25, 15, 5, 250, 50, 85, 500, 350, 100, '$' ; stock price
	total_sales dw 0
	
	; formatting
	one_line db 13,10, '==============================================' ,'$'
	dotted_line db '**********************************************','$'

	; menu
	menu db 13, '**********ERICKO INTEGRATED ARMORY TERMINAL**********',13,10, '<<<<<<<<<<<<"WHY 911 WHEN YOU HAVE 9MM?">>>>>>>>>>>>>',13,10, '----------------------DASHBOARD----------------------', 13, 10, 10 ,'1. View Items',13,10,'2. Restock Items',13,10,'3. Sell Items',13,10, '4. Sort Items',13,10,'5. Stock Report',13,10,'0. Exit the Program',13,10,'$'
	invalid_input db 13,10,'Invalid input!, please try again.',13,10,'$'
	
	; view items
	stock_header db 13,10, '**********ERICKO INTEGRATED ARMORY TERMINAL**********',13,10, '----------------<ARMORY GOODS>-----------------',13,10,'ID',9,'Name',9,9, 'Quantity',9, 'Credit',13,10,'$'
	stock_footer db '==============================================', 13, 10, 'Items that needs to be restocked are highlighted in RED!', 13, 10, '==============================================', 13, 10, '1. Main Menu', 13, 10,  '2. Restock Items', 13, 10, '3. Sell Items', 13, 10 , 13, 10,'Select your choice: $'	
	stock_amount dw ?
	stock_id dw ?

	; restock
	restock_header db '==============================================', 13, 10,9,9, 32,32,'RESTOCK', 13, 10, '==============================================', 13, 10, 'Select the desired item ID to restock: $'
	restock_footer db 13, 10, 'Select the amount of item to restock (min 1-9 max): $'
	restock_success db 13, 10, 'Item has been added to the armory!', 13, 10, '$'

	; sell items 
	sell_header db '==============================================', 13, 10,9,9, 32,32,'SELL STOCK', 13, 10, '==============================================', 13, 10,  'Select the desired item ID to sell: $'
	sell_footer db 13, 10, 'Select the amount of item to sell (min 1-9 max): $'
	sell_success db 13, 10, 'Item Sold!, Please contact our staff to claim your purchase', 13, 10, '$'
	sell_failed db 13, 10, 'Sorry, the item you select is out of stock!', 13, 10, '$'

	;categorize
	sort_footer db 13, '==============================================', 13, 10,9,'SORT STOCK', 13, 10, '==============================================', 13, 10, '1. Main Menu', 13, 10, '2. Available Items', 13, 10, '3. Restock Request', 13, 10, 13, 10, 'Select your choice: $'
	
	;sales
	sales_header db 13,10, '**********ERICKO INTEGRATED ARMORY TERMINAL**********',13,10, '----------------------------<STOCK REPORT>-------------------------',13,10,'ID',9,'Name',9,9, 'Amount Sold',9, 'Credit/Unit', 9, 'Total Earned',13,10,'$'
	sales_footer db '=================================================================', 13, 10, 9,9,32,32,9,'TOTAL ARMORY STOCK', 13, 10, '=================================================================', 13, 10, '1. Main Menu', 13, 10, '0. Exit Program', 13, 10 , 13, 10,'Select your choice: $'
	
    ; misc
	menu_option db 13, 10, 'Select your choice: $'
	menu_exit db 13, 10, 'Thank you for using Ericko integrated armory terminal :D ','$'

.code
main proc
	mov ax, @data ; set data segment
	mov ds, ax ; set data segment register
	
	call display_menu
	
	;Prompt user to select choice
	mov ah, 01h 
	int 21h
	
	;Check user input
	cmp al, '1'
	je view_stock_menu
	
	cmp al, '2'
	je restock_stock_menu
	
	cmp al, '3'
	je sales_stock_menu

	cmp al, '4'
	je sort_stock_menu
	
	cmp al, '5'
	je report_menu
	
	cmp al, '0'
	je quit_menu

	jmp main

;INTERFACE FUNCTIONS
	view_stock_menu:
		call reset_screen
		call view_stock
		call menu_display
		ret
	restock_stock_menu:
	    call reset_screen
		call view_stock
		call restock_stock
		ret
	sales_stock_menu:
	    call reset_screen
		call view_stock
		call sales_stock
		ret
	sort_stock_menu:
        call reset_screen
		call sort_stock
		call menu_display
		ret
	report_menu:
        call reset_screen
		call sales_report
		call sales_display
		ret
	quit_menu:
		call reset_screen
		call exit_program
		ret

;FUNCTIONS
menu_display:
	; Code to navigate user
	lea dx, stock_footer
	mov ah, 09h
	int 21h

	mov ah, 01h ; read character
	int 21h

	cmp al, '0'
	je quit_menu

	cmp al, '1'
	je main

	cmp al, '2'
	je restock_stock_menu
	
	cmp al, '3'
	je sales_stock_menu
	
	jmp main
	ret

sales_display:
	lea dx, sales_footer
	mov ah, 09h
	int 21h

	mov ah, 01h ; read character
	int 21h

	cmp al, '0'
	je quit_menu
	
	jmp main
	ret

print_integer:
	; convert the word to a string and print it
	push bx 
	mov bx, 10 
	xor cx, cx 
	convert_loop:
		xor dx, dx 
		div bx 
		add dl, '0' 
		push dx 
		inc cx
		cmp ax, 0
		jne convert_loop 
	print_loop2:
		pop dx 
		mov ah, 02 
		int 21h 
		dec cx 
		cmp cx, 0 
		jne print_loop2 
		pop bx 
		ret

check_integer:
	; check if integer is less than  5 or no
	mov bx, ax
	cmp bx, 5
	jle highlight_red ; if integer 5 and less, it is red
	ret

print_string:
	; Print string
	push ax 
	push bx
	push cx
	mov bx, dx 
	mov cx, 10 
	print_loop:
		mov dl, [bx] 
		int 21h 
		inc bx 
		loop print_loop 
	print_done:
	pop cx 
	pop bx
	pop ax
	ret

highlight_red:
	; highlight string in red
	push ax 
	push bx
	push cx
	mov bx, dx 
	mov cx, 10 
	print_loop3:
		mov dl, [bx] 
		mov ah, 09h
		mov al, dl 
		mov bl, 04h
		or bl, 80h
		int 10h
		inc bx 
		loop print_loop3 
	print_done3:
	pop cx 
	pop bx
	pop ax
	ret

; REQUIREMENTS FUNCTIONS 
display_menu:
	; Code to print menu
	call reset_screen
	lea dx, menu
	mov ah, 09h
	int 21h
	
	lea dx, menu_option
	mov ah, 09h
	int 21h
	ret

view_stock:
	; code to view stock 
	mov dx, offset stock_header
	mov ah, 09
	int 21h
	
	mov bp, 0
	lea si, stock

	loop_start:
		mov ax, [si] 
		cmp ax, 10 
		ja done 
		call print_integer 
		call print_tab

		mov dx, offset stock + 20 
		add dx, bp 
		call print_string 
		mov ax, [si + 120] 
		call check_integer 
		call print_tab
		
		mov ax, [si + 120] 
		call print_integer
		call print_doubletab
		
		mov ax, [si + 140]
		call print_integer
		call print_newline

		add bp, 10
		add si, 2 
		jmp loop_start 
	done:
	ret

restock_stock:
	; Code to restock item
	lea dx, restock_header
	mov ah, 09h
	int 21h 

	mov ah, 01
	int 21h

	sub al, 30h 
	add al, al
	sub ax, 136
	mov stock_id, ax 

	lea dx, restock_footer
	mov ah, 09h 
	int 21h

	mov ah, 01
	int 21h
	sub al, 30h
	sub ax, 256
	mov cx, ax

	lea si, stock
	add si, stock_id
	add cx, [si]
	mov word ptr [si], cx 
	
	call reset_screen
	call print_newline
	call print_dots
	lea dx, restock_success
	mov ah, 09h 
	int 21h 
	call print_dots
	call print_newline
	call view_stock
	call menu_display
	ret

sales_stock:
	; Code to sell item
	lea dx, sell_header
	mov ah, 09h
	int 21h 

	mov ah, 01
	int 21h

	sub al, 30h 
	add al, al 
	sub ax, 136 
	mov stock_id, ax 

	lea dx, sell_footer
	mov ah, 09h 
	int 21h

	mov ah, 01
	int 21h
	sub al, 30h
	sub ax, 256
	mov cx, ax

	lea si, stock
	add si, stock_id
	mov bx, [si] 
	sub bx, cx
	cmp bx, 0
	js reset_quantity

	mov word ptr [si], bx
	jmp sold_quantity

	reset_quantity: 
		mov bx, [si]
		mov word ptr [si], bx
		call reset_screen
		call print_newline
		call print_dots
		lea dx, sell_failed
		mov ah, 09h 
		int 21h 
		call print_dots
		call print_newline
		call view_stock
		call menu_display
		ret 
	
	sold_quantity:
	  call sales_done
		call reset_screen
		call print_newline
		call print_dots
		lea dx, sell_success
		mov ah, 09h 
		int 21h 
		call print_dots
		call print_newline
		call view_stock
		call menu_display
		ret
	sales_done: 
		mov ax, stock_id 
		sub ax, 120 
		mov stock_id, ax
		lea si, stock_sold 
		add si, stock_id
		mov ax, [si]
		add cx, ax 
		mov word ptr [si], cx
		ret
	ret

sort_stock:
	; Code to sort item
	call reset_screen
	lea dx, sort_footer
	mov ah, 09h 
	int 21h 
	
	mov ah, 01h 
	int 21h 
	 
	cmp al, '2'
	je in_stock
	
	cmp al, '3' 
	je low_stock 
	
	cmp al, '1'
	call main

	ret

in_stock:
    ; code to print out items in stock (>5)
	call reset_screen
	mov dx, offset stock_header
	mov ah, 09
	int 21h
	
	mov bp, 0
	lea si, stock

	loop_start2:
	  mov ax, [si] 
		cmp ax, 10 
		ja end2

		mov ax, [si + 120] 
		cmp ax, 6 
		jl done2 

		mov ax, [si]
		call print_integer 

		call print_tab

		mov dx, offset stock + 20 
		add dx, bp 
		call print_string 
		mov ax, [si + 120] 
		call check_integer 

		call print_tab
		
		mov ax, [si + 120] 
		call print_integer

		call print_doubletab
		
		mov ax, [si + 140]
		call print_integer
		call print_newline

		add bp, 10
		add si, 2 
		jmp loop_start2 
	done2:
	  add bp, 10
		add si, 2
		jmp loop_start2
		ret 
	end2:
	  ret
	ret

low_stock:
    ; code to print out items 5 and below (<=5)
	call reset_screen
	mov dx, offset stock_header
	mov ah, 09
	int 21h
	
	mov bp, 0
	lea si, stock

	loop_start3:
	  mov ax, [si] 
		cmp ax, 10 
		ja end3

		mov ax, [si + 120] 
		cmp ax, 5 
		jg done3

		mov ax, [si]
		call print_integer 

		call print_tab

		mov dx, offset stock + 20 
		add dx, bp 
		call print_string 
		mov ax, [si + 120] 
		call check_integer ; check if stock is low stock

		call print_tab
		
		mov ax, [si + 120] 
		call print_integer

		call print_doubletab
		
		mov ax, [si + 140]
		call print_integer
		call print_newline

		add bp, 10
		add si, 2 
		jmp loop_start3 
	done3:
	  add bp, 10
		add si, 2
		jmp loop_start3
		ret 
	end3:
	  ret
  ret 

sales_report:
    call reset_screen
	; Code to print report
	mov dx, offset sales_header
	mov ah, 09
	int 21h

    mov bp, 0
	lea si, stock
	mov bx, offset stock_sold 
	mov di, offset stock_credit

	loop_start5:
		mov ax, [si] 
		cmp ax, 10 
		ja done5 
		call print_integer 
		call print_tab

		mov dx, offset stock + 20 
		add dx, bp 
		call print_string 
		call print_tab

		mov ax, [bx]
		call print_integer
		call print_doubletab
	
	    mov ax, [si + 140]
		call print_integer	
	    call print_doubletab

		mov cx, [bx]
		mov ax, [di]
		mul cx
		call print_integer	
		call print_newline
        
        add bp, 10
		add si, 2 
		add bx, 2 
		add di, 2
		jmp loop_start5 
	done5:	  
	ret

; MISC FUNCTIONS 
exit_program:
	; Code to exit program
	call print_line

	lea dx, menu_exit
	mov ah, 09h
	int 21h 
	
	call print_line

	mov ah, 4ch
	int 21h

reset_screen:
	; Code to reset the screen
    mov ah, 06h
    mov al, 0
    mov bh, 07h
    mov cx, 0
    mov dx, 184Fh
    int 10h
    ret

print_line:
	lea dx, one_line
	mov ah, 09h
	int 21h
	ret

print_newline:
	mov dl, 0ah
	mov ah, 02
	int 21h
	ret

print_tab:
	mov dl, 09
	mov ah, 02
	int 21h
	ret

print_doubletab:
	mov dl, 09
	mov ah, 02
	int 21h

	mov dl, 09
	mov ah, 02
	int 21h
	ret

print_dots:
	lea dx, dotted_line
	mov ah, 09h 
	int 21h 
	ret

main endp
end main