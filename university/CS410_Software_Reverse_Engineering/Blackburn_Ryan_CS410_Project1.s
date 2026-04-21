	.file	"Blackburn_Ryan_CS410_Project1.cpp"
	.text
	.section	.rodata
	.type	_ZStL19piecewise_construct, @object
	.size	_ZStL19piecewise_construct, 1
_ZStL19piecewise_construct:
	.zero	1
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
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
	.string	"Created by Ryan Blackburn CS-410 Project 1\n"
	.align 8
.LC6:
	.string	"Hello! Welcome to our Investment Company\n"
	.align 8
.LC7:
	.string	"Invalid Password. Please try again\n"
.LC8:
	.string	"What would you like to do?\n"
	.align 8
.LC9:
	.string	"DISPLAY the client list (enter 1)\n"
	.align 8
.LC10:
	.string	"CHANGE a client's choice (enter 2)\n"
.LC11:
	.string	"Exit the program.. (enter 3)\n"
.LC12:
	.string	"You chose "
	.text
	.globl	main
	.type	main, @function
main:
.LFB1493:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	leaq	.LC5(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC6(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	call	_Z25CheckUserPermissionAccessv
	movl	%eax, answer(%rip)
	movl	answer(%rip), %eax
	cmpl	$1, %eax
	je	.L5
	leaq	.LC7(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
.L5:
	movl	answer(%rip), %eax
	cmpl	$1, %eax
	je	.L3
	call	_Z25CheckUserPermissionAccessv
	movl	%eax, answer(%rip)
	movl	answer(%rip), %eax
	cmpl	$1, %eax
	je	.L5
	leaq	.LC7(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	jmp	.L5
.L3:
	leaq	.LC8(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC9(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC10(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC11(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	choice(%rip), %rsi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZNSirsERi@PLT
	leaq	.LC12(%rip), %rsi
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
	jne	.L6
	call	_Z11DisplayInfov
	jmp	.L7
.L6:
	movl	choice(%rip), %eax
	cmpl	$2, %eax
	jne	.L7
	call	_Z20ChangeCustomerChoicev
.L7:
	movl	choice(%rip), %eax
	cmpl	$3, %eax
	je	.L12
	jmp	.L3
.L12:
	nop
	movl	$0, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1493:
	.size	main, .-main
	.section	.rodata
.LC13:
	.string	"Enter your username: \n"
.LC14:
	.string	"Enter your password: \n"
.LC15:
	.string	"123"
	.text
	.globl	_Z25CheckUserPermissionAccessv
	.type	_Z25CheckUserPermissionAccessv, @function
_Z25CheckUserPermissionAccessv:
.LFB1494:
	.cfi_startproc
	.cfi_personality 0x9b,DW.ref.__gxx_personality_v0
	.cfi_lsda 0x1b,.LLSDA1494
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
	leaq	.LC13(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
.LEHB0:
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	username(%rip), %rsi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_PS3_@PLT
	leaq	.LC14(%rip), %rsi
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
	leaq	.LC15(%rip), %rsi
	movq	%rax, %rdi
	call	_ZNKSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE7compareEPKc@PLT
	testl	%eax, %eax
	sete	%al
	testb	%al, %al
	je	.L14
	movl	$1, %ebx
	jmp	.L15
.L14:
	movl	$2, %ebx
.L15:
	leaq	-64(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@PLT
	movl	%ebx, %eax
	movq	-24(%rbp), %rdx
	xorq	%fs:40, %rdx
	je	.L18
	jmp	.L20
.L19:
	movq	%rax, %rbx
	leaq	-64(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@PLT
	movq	%rbx, %rax
	movq	%rax, %rdi
.LEHB2:
	call	_Unwind_Resume@PLT
.LEHE2:
.L20:
	call	__stack_chk_fail@PLT
.L18:
	addq	$56, %rsp
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1494:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA1494:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1494-.LLSDACSB1494
.LLSDACSB1494:
	.uleb128 .LEHB0-.LFB1494
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB1494
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L19-.LFB1494
	.uleb128 0
	.uleb128 .LEHB2-.LFB1494
	.uleb128 .LEHE2-.LEHB2
	.uleb128 0
	.uleb128 0
.LLSDACSE1494:
	.text
	.size	_Z25CheckUserPermissionAccessv, .-_Z25CheckUserPermissionAccessv
	.section	.rodata
	.align 8
.LC16:
	.string	"  Client's Name    Service Selected (1 = Brokerage, 2 = Retirement)"
.LC17:
	.string	"1. "
.LC18:
	.string	" selected option "
.LC19:
	.string	"2. "
.LC20:
	.string	"3. "
.LC21:
	.string	"4. "
.LC22:
	.string	"5. "
	.text
	.globl	_Z11DisplayInfov
	.type	_Z11DisplayInfov, @function
_Z11DisplayInfov:
.LFB1495:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	leaq	.LC16(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GOTPCREL(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZNSolsEPFRSoS_E@PLT
	leaq	.LC17(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	name1(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC18(%rip), %rsi
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
	leaq	.LC19(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	name2(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC18(%rip), %rsi
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
	leaq	.LC20(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	name3(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC18(%rip), %rsi
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
	leaq	.LC21(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	name4(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC18(%rip), %rsi
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
	leaq	.LC22(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movq	%rax, %rdx
	movq	name5(%rip), %rax
	movq	%rax, %rsi
	movq	%rdx, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC18(%rip), %rsi
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
.LFE1495:
	.size	_Z11DisplayInfov, .-_Z11DisplayInfov
	.section	.rodata
	.align 8
.LC23:
	.string	"Enter the number of the client that you wish to change\n"
	.align 8
.LC24:
	.string	"Please enter the client's new service choice (1 = Brokerage, 2 = Retirement)\n"
	.text
	.globl	_Z20ChangeCustomerChoicev
	.type	_Z20ChangeCustomerChoicev, @function
_Z20ChangeCustomerChoicev:
.LFB1496:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	leaq	.LC23(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	changechoice(%rip), %rsi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZNSirsERi@PLT
	leaq	.LC24(%rip), %rsi
	leaq	_ZSt4cout(%rip), %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	newservice(%rip), %rsi
	leaq	_ZSt3cin(%rip), %rdi
	call	_ZNSirsERi@PLT
	movl	changechoice(%rip), %eax
	cmpl	$1, %eax
	jne	.L23
	movl	newservice(%rip), %eax
	movl	%eax, num1(%rip)
	jmp	.L28
.L23:
	movl	changechoice(%rip), %eax
	cmpl	$2, %eax
	jne	.L25
	movl	newservice(%rip), %eax
	movl	%eax, num2(%rip)
	jmp	.L28
.L25:
	movl	changechoice(%rip), %eax
	cmpl	$3, %eax
	jne	.L26
	movl	newservice(%rip), %eax
	movl	%eax, num3(%rip)
	jmp	.L28
.L26:
	movl	changechoice(%rip), %eax
	cmpl	$4, %eax
	jne	.L27
	movl	newservice(%rip), %eax
	movl	%eax, num4(%rip)
	jmp	.L28
.L27:
	movl	changechoice(%rip), %eax
	cmpl	$5, %eax
	jne	.L28
	movl	newservice(%rip), %eax
	movl	%eax, num5(%rip)
.L28:
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1496:
	.size	_Z20ChangeCustomerChoicev, .-_Z20ChangeCustomerChoicev
	.type	_Z41__static_initialization_and_destruction_0ii, @function
_Z41__static_initialization_and_destruction_0ii:
.LFB1988:
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
	jne	.L31
	cmpl	$65535, -8(%rbp)
	jne	.L31
	leaq	_ZStL8__ioinit(%rip), %rdi
	call	_ZNSt8ios_base4InitC1Ev@PLT
	leaq	__dso_handle(%rip), %rdx
	leaq	_ZStL8__ioinit(%rip), %rsi
	movq	_ZNSt8ios_base4InitD1Ev@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	__cxa_atexit@PLT
.L31:
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1988:
	.size	_Z41__static_initialization_and_destruction_0ii, .-_Z41__static_initialization_and_destruction_0ii
	.type	_GLOBAL__sub_I_username, @function
_GLOBAL__sub_I_username:
.LFB1989:
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
.LFE1989:
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
