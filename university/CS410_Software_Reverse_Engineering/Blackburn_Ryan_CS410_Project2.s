	.file	"Blackburn_Ryan_CS410_Project2.cpp"
	.text
	.section	.rodata
	.type	_ZStL19piecewise_construct, @object
	.size	_ZStL19piecewise_construct, 1
_ZStL19piecewise_construct:
	.zero	1
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.section	.text._ZNSt14numeric_limitsIlE3maxEv,"axG",@progbits,_ZNSt14numeric_limitsIlE3maxEv,comdat
	.weak	_ZNSt14numeric_limitsIlE3maxEv
	.type	_ZNSt14numeric_limitsIlE3maxEv, @function
_ZNSt14numeric_limitsIlE3maxEv:
.LFB1602:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movabsq	$9223372036854775807, %rax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1602:
	.size	_ZNSt14numeric_limitsIlE3maxEv, .-_ZNSt14numeric_limitsIlE3maxEv
	.section	.rodata
	.type	_ZStL13allocator_arg, @object
	.size	_ZStL13allocator_arg, 1
_ZStL13allocator_arg:
	.zero	1
	.type	_ZStL6ignore, @object
	.size	_ZStL6ignore, 1
_ZStL6ignore:
	.zero	1
	.section	.text._ZSt4setwi,"axG",@progbits,_ZSt4setwi,comdat
	.weak	_ZSt4setwi
	.type	_ZSt4setwi, @function
_ZSt4setwi:
.LFB2246:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, -4(%rbp)
	movl	-4(%rbp), %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2246:
	.size	_ZSt4setwi, .-_ZSt4setwi
	.globl	username
	.bss
	.align 32
	.type	username, @object
	.size	username, 64
username:
	.zero	64
	.globl	answer
	.align 4
	.type	answer, @object
	.size	answer, 4
answer:
	.zero	4
	.globl	choice
	.align 4
	.type	choice, @object
	.size	choice, 4
choice:
	.zero	4
	.globl	changechoice
	.align 4
	.type	changechoice, @object
	.size	changechoice, 4
changechoice:
	.zero	4
	.globl	newservice
	.align 4
	.type	newservice, @object
	.size	newservice, 4
newservice:
	.zero	4
	.globl	name1
	.section	.rodata
.LC0:
	.string	"Client One"
	.section	.data.rel.local,"aw",@progbits
	.align 8
	.type	name1, @object
	.size	name1, 8
name1:
	.quad	.LC0
	.globl	name2
	.section	.rodata
.LC1:
	.string	"Client Two"
	.section	.data.rel.local
	.align 8
	.type	name2, @object
	.size	name2, 8
name2:
	.quad	.LC1
	.globl	name3
	.section	.rodata
.LC2:
	.string	"Client Three"
	.section	.data.rel.local
	.align 8
	.type	name3, @object
	.size	name3, 8
name3:
	.quad	.LC2
	.globl	name4
	.section	.rodata
.LC3:
	.string	"Client Four"
	.section	.data.rel.local
	.align 8
	.type	name4, @object
	.size	name4, 8
name4:
	.quad	.LC3
	.globl	name5
	.section	.rodata
.LC4:
	.string	"Client Five"
	.section	.data.rel.local
	.align 8
	.type	name5, @object
	.size	name5, 8
name5:
	.quad	.LC4
	.globl	num1
	.data
	.align 4
	.type	num1, @object
	.size	num1, 4
num1:
	.long	1
	.globl	num2
	.align 4
	.type	num2, @object
	.size	num2, 4
num2:
	.long	2
	.globl	num3
	.align 4
	.type	num3, @object
	.size	num3, 4
num3:
	.long	1
	.globl	num4
	.align 4
	.type	num4, @object
	.size	num4, 4
num4:
	.long	2
	.globl	num5
	.align 4
	.type	num5, @object
	.size	num5, 4
num5:
	.long	1
	.section	.rodata
	.align 8
.LC5:
	.string	"Created by Ryan Blackburn CS-410 Project 2\n"
	.align 8
.LC6:
	.string	"Hello! Welcome to our Investment Company\n"
	.align 8
.LC7:
	.string	"Invalid Password. Please try again\n"
	.align 8
.LC8:
	.string	"Too many failed login attempts. Exiting program.\n"
.LC9:
	.string	"What would you like to do?\n"
	.align 8
.LC10:
	.string	"DISPLAY the client list (enter 1)\n"
	.align 8
.LC11:
	.string	"CHANGE a client's choice (enter 2)\n"
.LC12:
	.string	"Exit the program.. (enter 3)\n"
	.align 8
.LC13:
	.string	"Invalid input. Please enter a number (1-3).\n"
	.align 8
.LC14:
	.string	"Invalid choice. Please enter 1, 2, or 3.\n"
.LC15:
	.string	"You chose "
	.text
	.globl	main
	.type	main, @function
main:
.LFB2260:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	leaq	.LC5(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC6(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$3, -4(%rbp)
	movl	$0, -8(%rbp)
	call	_Z25CheckUserPermissionAccessv
	movl	%eax, answer(%rip)
	addl	$1, -8(%rbp)
	movl	answer(%rip), %eax
	cmpl	$1, %eax
	je	.L9
	leaq	.LC7(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
.L9:
	movl	answer(%rip), %eax
	cmpl	$1, %eax
	je	.L7
	cmpl	$2, -8(%rbp)
	jg	.L7
	call	_Z25CheckUserPermissionAccessv
	movl	%eax, answer(%rip)
	addl	$1, -8(%rbp)
	movl	answer(%rip), %eax
	cmpl	$1, %eax
	je	.L9
	leaq	.LC7(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	jmp	.L9
.L7:
	movl	answer(%rip), %eax
	cmpl	$1, %eax
	je	.L10
	leaq	.LC8(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %eax
	jmp	.L11
.L10:
	leaq	.LC9(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC10(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC11(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC12(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	choice(%rip), %rsi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZNSirsERi@PLT
	leaq	16+_ZSt3cin(%rip), %rdi
	call	_ZNKSt9basic_iosIcSt11char_traitsIcEE4failEv@PLT
	testb	%al, %al
	je	.L12
	movl	$0, %esi
	leaq	16+_ZSt3cin(%rip), %rdi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate@PLT
	call	_ZNSt14numeric_limitsIlE3maxEv
	movl	$10, %edx
	movq	%rax, %rsi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZNSi6ignoreEli@PLT
	leaq	.LC13(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	jmp	.L13
.L12:
	movl	choice(%rip), %eax
	testl	%eax, %eax
	jle	.L14
	movl	choice(%rip), %eax
	cmpl	$3, %eax
	jle	.L15
.L14:
	leaq	.LC14(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	jmp	.L13
.L15:
	leaq	.LC15(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movl	choice(%rip), %eax
	movl	%eax, %esi
	movq	%rdx, %rdi
	call	_ZNSolsEi@PLT
	movq	%rax, %rdx
	movq	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GOTPCREL(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZNSolsEPFRSoS_E@PLT
	movl	choice(%rip), %eax
	cmpl	$1, %eax
	jne	.L16
	call	_Z11DisplayInfov
	jmp	.L17
.L16:
	movl	choice(%rip), %eax
	cmpl	$2, %eax
	jne	.L17
	call	_Z20ChangeCustomerChoicev
.L17:
	movl	choice(%rip), %eax
	cmpl	$3, %eax
	je	.L20
.L13:
	jmp	.L10
.L20:
	nop
	movl	$0, %eax
.L11:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2260:
	.size	main, .-main
	.section	.rodata
.LC16:
	.string	"Enter your username: \n"
.LC17:
	.string	"Enter your password: \n"
.LC18:
	.string	"123"
	.text
	.globl	_Z25CheckUserPermissionAccessv
	.type	_Z25CheckUserPermissionAccessv, @function
_Z25CheckUserPermissionAccessv:
.LFB2261:
	.cfi_startproc
	.cfi_personality 0x9b,DW.ref.__gxx_personality_v0
	.cfi_lsda 0x1b,.LLSDA2261
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$56, %rsp
	.cfi_offset 3, -24
	movq	%fs:40, %rax
	movq	%rax, -24(%rbp)
	xorl	%eax, %eax
	leaq	.LC16(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
.LEHB0:
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$64, %edi
	call	_ZSt4setwi
	movl	%eax, %esi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_St5_Setw@PLT
	leaq	username(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_PS3_@PLT
	leaq	.LC17(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
.LEHE0:
	leaq	-64(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1Ev@PLT
	leaq	-64(%rbp), %rax
	movq	%rax, %rsi
	leaq	_ZSt3cin(%rip), %rdi
.LEHB1:
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE@PLT
.LEHE1:
	leaq	-64(%rbp), %rax
	leaq	.LC18(%rip), %rsi
	movq	%rax, %rdi
	call	_ZNKSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE7compareEPKc@PLT
	testl	%eax, %eax
	sete	%al
	testb	%al, %al
	je	.L22
	movl	$1, %ebx
	jmp	.L23
.L22:
	movl	$2, %ebx
.L23:
	leaq	-64(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@PLT
	movl	%ebx, %eax
	movq	-24(%rbp), %rdx
	xorq	%fs:40, %rdx
	je	.L26
	jmp	.L28
.L27:
	movq	%rax, %rbx
	leaq	-64(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@PLT
	movq	%rbx, %rax
	movq	%rax, %rdi
.LEHB2:
	call	_Unwind_Resume@PLT
.LEHE2:
.L28:
	call	__stack_chk_fail@PLT
.L26:
	addq	$56, %rsp
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2261:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA2261:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE2261-.LLSDACSB2261
.LLSDACSB2261:
	.uleb128 .LEHB0-.LFB2261
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB2261
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L27-.LFB2261
	.uleb128 0
	.uleb128 .LEHB2-.LFB2261
	.uleb128 .LEHE2-.LEHB2
	.uleb128 0
	.uleb128 0
.LLSDACSE2261:
	.text
	.size	_Z25CheckUserPermissionAccessv, .-_Z25CheckUserPermissionAccessv
	.section	.rodata
	.align 8
.LC19:
	.string	"  Client's Name    Service Selected (1 = Brokerage, 2 = Retirement)"
.LC20:
	.string	"1. "
.LC21:
	.string	" selected option "
.LC22:
	.string	"2. "
.LC23:
	.string	"3. "
.LC24:
	.string	"4. "
.LC25:
	.string	"5. "
	.text
	.globl	_Z11DisplayInfov
	.type	_Z11DisplayInfov, @function
_Z11DisplayInfov:
.LFB2262:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	leaq	.LC19(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GOTPCREL(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZNSolsEPFRSoS_E@PLT
	leaq	.LC20(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	name1(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC21(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movl	num1(%rip), %eax
	movl	%eax, %esi
	movq	%rdx, %rdi
	call	_ZNSolsEi@PLT
	movq	%rax, %rdx
	movq	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GOTPCREL(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZNSolsEPFRSoS_E@PLT
	leaq	.LC22(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	name2(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC21(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movl	num2(%rip), %eax
	movl	%eax, %esi
	movq	%rdx, %rdi
	call	_ZNSolsEi@PLT
	movq	%rax, %rdx
	movq	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GOTPCREL(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZNSolsEPFRSoS_E@PLT
	leaq	.LC23(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	name3(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC21(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movl	num3(%rip), %eax
	movl	%eax, %esi
	movq	%rdx, %rdi
	call	_ZNSolsEi@PLT
	movq	%rax, %rdx
	movq	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GOTPCREL(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZNSolsEPFRSoS_E@PLT
	leaq	.LC24(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	name4(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC21(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movl	num4(%rip), %eax
	movl	%eax, %esi
	movq	%rdx, %rdi
	call	_ZNSolsEi@PLT
	movq	%rax, %rdx
	movq	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GOTPCREL(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZNSolsEPFRSoS_E@PLT
	leaq	.LC25(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	name5(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC21(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movl	num5(%rip), %eax
	movl	%eax, %esi
	movq	%rdx, %rdi
	call	_ZNSolsEi@PLT
	movq	%rax, %rdx
	movq	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GOTPCREL(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZNSolsEPFRSoS_E@PLT
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2262:
	.size	_Z11DisplayInfov, .-_Z11DisplayInfov
	.section	.rodata
	.align 8
.LC26:
	.string	"Enter the number of the client that you wish to change\n"
	.align 8
.LC27:
	.string	"Invalid input. Client number must be 1-5.\n"
	.align 8
.LC28:
	.string	"Invalid client selection. Please choose a number from 1 to 5.\n"
	.align 8
.LC29:
	.string	"Please enter the client's new service choice (1 = Brokerage, 2 = Retirement)\n"
	.align 8
.LC30:
	.string	"Invalid input. Service choice must be 1 or 2.\n"
	.align 8
.LC31:
	.string	"Invalid service selection. Please enter 1 (Brokerage) or 2 (Retirement).\n"
.LC32:
	.string	"Invalid client selection.\n"
	.text
	.globl	_Z20ChangeCustomerChoicev
	.type	_Z20ChangeCustomerChoicev, @function
_Z20ChangeCustomerChoicev:
.LFB2263:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	leaq	.LC26(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	changechoice(%rip), %rsi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZNSirsERi@PLT
	leaq	16+_ZSt3cin(%rip), %rdi
	call	_ZNKSt9basic_iosIcSt11char_traitsIcEE4failEv@PLT
	testb	%al, %al
	je	.L31
	movl	$0, %esi
	leaq	16+_ZSt3cin(%rip), %rdi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate@PLT
	call	_ZNSt14numeric_limitsIlE3maxEv
	movl	$10, %edx
	movq	%rax, %rsi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZNSi6ignoreEli@PLT
	leaq	.LC27(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	jmp	.L30
.L31:
	movl	changechoice(%rip), %eax
	testl	%eax, %eax
	jle	.L33
	movl	changechoice(%rip), %eax
	cmpl	$5, %eax
	jle	.L34
.L33:
	leaq	.LC28(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	jmp	.L30
.L34:
	leaq	.LC29(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	newservice(%rip), %rsi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZNSirsERi@PLT
	leaq	16+_ZSt3cin(%rip), %rdi
	call	_ZNKSt9basic_iosIcSt11char_traitsIcEE4failEv@PLT
	testb	%al, %al
	je	.L35
	movl	$0, %esi
	leaq	16+_ZSt3cin(%rip), %rdi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate@PLT
	call	_ZNSt14numeric_limitsIlE3maxEv
	movl	$10, %edx
	movq	%rax, %rsi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZNSi6ignoreEli@PLT
	leaq	.LC30(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	jmp	.L30
.L35:
	movl	newservice(%rip), %eax
	cmpl	$1, %eax
	je	.L36
	movl	newservice(%rip), %eax
	cmpl	$2, %eax
	je	.L36
	leaq	.LC31(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	jmp	.L30
.L36:
	movl	changechoice(%rip), %eax
	cmpl	$1, %eax
	jne	.L37
	movl	newservice(%rip), %eax
	movl	%eax, num1(%rip)
	jmp	.L30
.L37:
	movl	changechoice(%rip), %eax
	cmpl	$2, %eax
	jne	.L38
	movl	newservice(%rip), %eax
	movl	%eax, num2(%rip)
	jmp	.L30
.L38:
	movl	changechoice(%rip), %eax
	cmpl	$3, %eax
	jne	.L39
	movl	newservice(%rip), %eax
	movl	%eax, num3(%rip)
	jmp	.L30
.L39:
	movl	changechoice(%rip), %eax
	cmpl	$4, %eax
	jne	.L40
	movl	newservice(%rip), %eax
	movl	%eax, num4(%rip)
	jmp	.L30
.L40:
	movl	changechoice(%rip), %eax
	cmpl	$5, %eax
	jne	.L41
	movl	newservice(%rip), %eax
	movl	%eax, num5(%rip)
	jmp	.L30
.L41:
	leaq	.LC32(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
.L30:
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2263:
	.size	_Z20ChangeCustomerChoicev, .-_Z20ChangeCustomerChoicev
	.type	_Z41__static_initialization_and_destruction_0ii, @function
_Z41__static_initialization_and_destruction_0ii:
.LFB2771:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movl	%esi, -8(%rbp)
	cmpl	$1, -4(%rbp)
	jne	.L44
	cmpl	$65535, -8(%rbp)
	jne	.L44
	leaq	_ZStL8__ioinit(%rip), %rdi
	call	_ZNSt8ios_base4InitC1Ev@PLT
	leaq	__dso_handle(%rip), %rdx
	leaq	_ZStL8__ioinit(%rip), %rsi
	movq	_ZNSt8ios_base4InitD1Ev@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	__cxa_atexit@PLT
.L44:
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2771:
	.size	_Z41__static_initialization_and_destruction_0ii, .-_Z41__static_initialization_and_destruction_0ii
	.type	_GLOBAL__sub_I_username, @function
_GLOBAL__sub_I_username:
.LFB2772:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$65535, %esi
	movl	$1, %edi
	call	_Z41__static_initialization_and_destruction_0ii
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2772:
	.size	_GLOBAL__sub_I_username, .-_GLOBAL__sub_I_username
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_username
	.hidden	DW.ref.__gxx_personality_v0
	.weak	DW.ref.__gxx_personality_v0
	.section	.data.rel.local.DW.ref.__gxx_personality_v0,"awG",@progbits,DW.ref.__gxx_personality_v0,comdat
	.align 8
	.type	DW.ref.__gxx_personality_v0, @object
	.size	DW.ref.__gxx_personality_v0, 8
DW.ref.__gxx_personality_v0:
	.quad	__gxx_personality_v0
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
