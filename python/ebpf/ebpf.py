#!/usr/bin/env python

from bcc import BPF

# This may not work for 4.17 on x64, you need replace kprobe__sys_clone with kprobe____x64_sys_clone
prog = """
	int kprobe__sys_clone(void *ctx) {
		bpf_trace_printk("Hello, World!\\n");
		return 0;
	}
"""

b = BPF(text=prog, debug=0x04)
b.trace_print()

# https://cloudnative.to/blog/bpf-intro/#2-ebpf

# https://feisky.gitbooks.io/sdn/content/linux/bpf/bcc.html

# https://github.com/iovisor/bcc/tree/master/tools
