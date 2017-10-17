{
    'variables':{
		'library' : 'static_library',
		#'library' : 'shared_library',
	},
    'target_defaults': {
		'win_delay_load_hook': 'false',
		'msvs_settings': {
			# This magical incantation is necessary because VC++ will compile
			# object files to same directory... even if they have the same name!
			'VCCLCompilerTool': {
			  'ObjectFile': '$(IntDir)/%(RelativeDir)/',
			  #'AdditionalOptions': [ '/EHsc', '/wd4244']
			  'WarningLevel': 0,
			  'WholeProgramOptimization': 'false',
			  'AdditionalOptions': ['/EHsc'],
			  'ExceptionHandling' : 1, #/EHsc
			},
			
		},
		'configurations':{
			'Debug':{
				'conditions': [
				  ['target_arch=="x64"', {
					'msvs_configuration_platform': 'x64',
				  }],
				  ['1==1',{

					'defines':[
						'DEBUG',
					],
					'msvs_settings': {		
						'VCCLCompilerTool': {
						  #'WholeProgramOptimization' : 'false',
						  #'AdditionalOptions': ['/GL-','/w'], #['/wd4244' ,'/wd4018','/wd4133' ,'/wd4090'] #GL- was added because the forced optimization coming from node-gyp is disturbing the weird coding style from ffmpeg.
						  'WarningLevel': 0,
						  'WholeProgramOptimization': 'false',
						  'AdditionalOptions': ['/EHsc'],
						  'ExceptionHandling' : 1, #/EHsc
						  'RuntimeLibrary': 3, # dll debug
						},
						'VCLinkerTool' : {
							'GenerateDebugInformation' : 'true',
							'conditions':[
								['target_arch=="x64"', {
									'TargetMachine' : 17 # /MACHINE:X64
								}],
							],
							
						}
					}
				
				  }],
				],
				
			},
			'Release':{
				'conditions': [
				  ['target_arch=="x64"', {
					'msvs_configuration_platform': 'x64',
				  }],
				],
				'msvs_settings': {			
					'VCCLCompilerTool': {
						'WholeProgramOptimization' : 'false',
						#'AdditionalOptions': ['/GL-','/w'], #['/wd4244' ,'/wd4018','/wd4133' ,'/wd4090'] #GL- was added because the forced optimization coming from node-gyp is disturbing the weird coding style from ffmpeg.
						'WarningLevel': 0,
						  'WholeProgramOptimization': 'false',
						  'AdditionalOptions': ['/EHsc'],
						  'ExceptionHandling' : 1, #/EHsc
						  'RuntimeLibrary': 2, # dll release
					},
					'VCLinkerTool' : {
						'conditions':[
							['target_arch=="x64"', {
								'TargetMachine' : 17 # /MACHINE:X64
							}],
						],
						
					}
				}
			},
		},
		
		'conditions': [
			['OS == "win"',{
				'defines':[
                    'WIN32',
					'DELAYIMP_INSECURE_WRITABLE_HOOKS'
				],
			}],
		  ['OS != "win"', {
			'defines': [
			  '_LARGEFILE_SOURCE',
			  '_FILE_OFFSET_BITS=64',
			  
			],
			'cflags':[
				'-fPIC',
				'-fexceptions',
			],
			'cflags!': [ '-fno-exceptions' ],
			'cflags_cc!': [ '-fno-exceptions' ],
			'conditions': [
				['OS=="mac"', {
				  'xcode_settings': {
					'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
				  }
				}]
			],
			'conditions': [
			  ['OS=="solaris"', {
				'cflags': [ '-pthreads' ],
			  }],
			  ['OS not in "solaris android"', {
				'cflags': [ '-pthread' ],
			  }],
			],
		}],
		['OS=="android"',{
			'defines':[
				'ANDROID'
			],
		  }],
		],
	  },

    'targets':[
        {
            "target_name":"kj",
            'type':'<(library)',
            'defines':[	
            ],
            'include_dirs':[
                'config',
                "src/c++/src",
                #"src/c++/src/kj",
            ],
            'dependencies':[
                #'copy_non_standard_extensions'
            ],
            'all_dependent_settings': {
                'include_dirs': [
                    "src/c++/src",
                    #"src/c++/src/kj",
                ],
            },
            'conditions':[
				['OS != "win"',{
					'sources':[
					],
					'link_settings':{
						'libraries':[
						],
					},
				}],
				['OS == "win"',{
					'link_settings': {
						'libraries': [
							'-lws2_32.lib',
                            '-lAdvapi32.lib'
						]
					}
				}]
				
			],
            
            'sources':[
                "src/c++/src/kj/arena-test.cpp",
                "src/c++/src/kj/arena.cpp",
                "src/c++/src/kj/arena.h",
                "src/c++/src/kj/array-test.cpp",
                "src/c++/src/kj/array.cpp",
                "src/c++/src/kj/array.h",
                "src/c++/src/kj/async-inl.h",
                "src/c++/src/kj/async-io-internal.h",
                "src/c++/src/kj/async-io-test.cpp",
                "src/c++/src/kj/async-io-unix.cpp",
                "src/c++/src/kj/async-io-win32.cpp",
                "src/c++/src/kj/async-io.cpp",
                "src/c++/src/kj/async-io.h",
                "src/c++/src/kj/async-prelude.h",
                "src/c++/src/kj/async-test.cpp",
                "src/c++/src/kj/async-unix-test.cpp",
                "src/c++/src/kj/async-unix.cpp",
                "src/c++/src/kj/async-unix.h",
                "src/c++/src/kj/async-win32-test.cpp",
                "src/c++/src/kj/async-win32.cpp",
                "src/c++/src/kj/async-win32.h",
                "src/c++/src/kj/async.cpp",
                "src/c++/src/kj/async.h",
                "src/c++/src/kj/common-test.cpp",
                "src/c++/src/kj/common.cpp",
                "src/c++/src/kj/common.h",
                "src/c++/src/kj/compat",
                "src/c++/src/kj/compat/gtest.h",
                "src/c++/src/kj/compat/gzip-test.cpp",
                "src/c++/src/kj/compat/gzip.cpp",
                "src/c++/src/kj/compat/gzip.h",
                "src/c++/src/kj/compat/http-test.cpp",
                "src/c++/src/kj/compat/http.cpp",
                "src/c++/src/kj/compat/http.h",
                "src/c++/src/kj/compat/make-test-certs.sh",
                "src/c++/src/kj/compat/readiness-io-test.cpp",
                "src/c++/src/kj/compat/readiness-io.cpp",
                "src/c++/src/kj/compat/readiness-io.h",
                "src/c++/src/kj/compat/tls-test.cpp",
                "src/c++/src/kj/compat/tls.cpp",
                "src/c++/src/kj/compat/tls.h",
                "src/c++/src/kj/compat/url-test.cpp",
                "src/c++/src/kj/compat/url.cpp",
                "src/c++/src/kj/compat/url.h",
                "src/c++/src/kj/debug-test.cpp",
                "src/c++/src/kj/debug.cpp",
                "src/c++/src/kj/debug.h",
                "src/c++/src/kj/encoding-test.cpp",
                "src/c++/src/kj/encoding.cpp",
                "src/c++/src/kj/encoding.h",
                "src/c++/src/kj/exception-test.cpp",
                "src/c++/src/kj/exception.cpp",
                "src/c++/src/kj/exception.h",
                #"src/c++/src/kj/filesystem-disk-generic-test.cpp",
                "src/c++/src/kj/filesystem-disk-old-kernel-test.cpp",
                #"src/c++/src/kj/filesystem-disk-test.cpp",
                #"src/c++/src/kj/filesystem-disk.cpp",
                "src/c++/src/kj/filesystem-test.cpp",
                "src/c++/src/kj/filesystem.cpp",
                "src/c++/src/kj/filesystem.h",
                "src/c++/src/kj/function-test.cpp",
                "src/c++/src/kj/function.h",
                "src/c++/src/kj/io-test.cpp",
                "src/c++/src/kj/io.cpp",
                "src/c++/src/kj/io.h",
                "src/c++/src/kj/main.cpp",
                "src/c++/src/kj/main.h",
                "src/c++/src/kj/memory-test.cpp",
                "src/c++/src/kj/memory.cpp",
                "src/c++/src/kj/memory.h",
                "src/c++/src/kj/miniposix.h",
                "src/c++/src/kj/mutex-test.cpp",
                "src/c++/src/kj/mutex.cpp",
                "src/c++/src/kj/mutex.h",
                "src/c++/src/kj/one-of-test.cpp",
                "src/c++/src/kj/one-of.h",
                "src/c++/src/kj/parse",
                "src/c++/src/kj/parse/char-test.cpp",
                "src/c++/src/kj/parse/char.cpp",
                "src/c++/src/kj/parse/char.h",
                "src/c++/src/kj/parse/common-test.cpp",
                "src/c++/src/kj/parse/common.h",
                "src/c++/src/kj/refcount-test.cpp",
                "src/c++/src/kj/refcount.cpp",
                "src/c++/src/kj/refcount.h",
                "src/c++/src/kj/std",
                "src/c++/src/kj/std/iostream-test.cpp",
                "src/c++/src/kj/std/iostream.h",
                "src/c++/src/kj/string-test.cpp",
                "src/c++/src/kj/string-tree-test.cpp",
                "src/c++/src/kj/string-tree.cpp",
                "src/c++/src/kj/string-tree.h",
                "src/c++/src/kj/string.cpp",
                "src/c++/src/kj/string.h",
                "src/c++/src/kj/test-helpers.cpp",
                "src/c++/src/kj/test-test.cpp",
                #"src/c++/src/kj/test.cpp",
                "src/c++/src/kj/test.h",
                "src/c++/src/kj/thread-test.cpp",
                "src/c++/src/kj/thread.cpp",
                "src/c++/src/kj/thread.h",
                "src/c++/src/kj/threadlocal-pthread-test.cpp",
                "src/c++/src/kj/threadlocal-test.cpp",
                "src/c++/src/kj/threadlocal.h",
                "src/c++/src/kj/time.cpp",
                "src/c++/src/kj/time.h",
                "src/c++/src/kj/tuple-test.cpp",
                "src/c++/src/kj/tuple.h",
                "src/c++/src/kj/units-test.cpp",
                "src/c++/src/kj/units.cpp",
                "src/c++/src/kj/units.h",
                "src/c++/src/kj/vector.h",
                "src/c++/src/kj/windows-sanity.h",
            ]
        },
        {
            "target_name":"capnp-compiler-dependencies",
            'type':'static_library',
            'defines':[	
            ],
            'include_dirs':[
                'config',
                "src\c++\src",
            ],
            'dependencies':[
                #'copy_non_standard_extensions',
                'kj',
                'libcapnp',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    "src\c++\src",
                ],
            },
            
            'sources':[
                "src/c++/src/capnp/compiler/compiler.cpp",
                "src/c++/src/capnp/compiler/compiler.h",
                "src/c++/src/capnp/compiler/error-reporter.cpp",
                "src/c++/src/capnp/compiler/error-reporter.h",
                #"src/c++/src/capnp/compiler/evolution-test.cpp",
                "src/c++/src/capnp/compiler/grammar.capnp",
                "src/c++/src/capnp/compiler/grammar.capnp.cpp",
                "src/c++/src/capnp/compiler/grammar.capnp.h",
                #"src/c++/src/capnp/compiler/lexer-test.cpp",
                "src/c++/src/capnp/compiler/lexer.cpp",
                "src/c++/src/capnp/compiler/lexer.capnp",
                "src/c++/src/capnp/compiler/lexer.capnp.cpp",
                "src/c++/src/capnp/compiler/lexer.capnp.h",
                "src/c++/src/capnp/compiler/lexer.h",
                "src/c++/src/capnp/compiler/module-loader.cpp",
                "src/c++/src/capnp/compiler/module-loader.h",
                "src/c++/src/capnp/compiler/node-translator.cpp",
                "src/c++/src/capnp/compiler/node-translator.h",
                "src/c++/src/capnp/compiler/parser.cpp",
                "src/c++/src/capnp/compiler/parser.h",
                #"src/c++/src/capnp/compiler/type-id-test.cpp",
                "src/c++/src/capnp/compiler/type-id.cpp",
                "src/c++/src/capnp/compiler/type-id.h",


                ##"src/c++/src/capnp/afl-testcase.cpp",
                ##"src/c++/src/capnp/any-test.cpp",
                #"src/c++/src/capnp/any.cpp",
                #"src/c++/src/capnp/any.h",
                #"src/c++/src/capnp/arena.cpp",
                #"src/c++/src/capnp/arena.h",
                ##"src/c++/src/capnp/blob-test.cpp",
                #"src/c++/src/capnp/blob.cpp",
                #"src/c++/src/capnp/blob.h",
                #"src/c++/src/capnp/bootstrap-test.ekam-rule",
                #"src/c++/src/capnp/c++.capnp",
                #"src/c++/src/capnp/c++.capnp.cpp",
                #"src/c++/src/capnp/c++.capnp.h",
                ##"src/c++/src/capnp/canonicalize-test.cpp",
                ##"src/c++/src/capnp/capability-test.cpp",
                #"src/c++/src/capnp/capability.cpp",
                #"src/c++/src/capnp/capability.h",
                #"src/c++/src/capnp/capnpc.ekam-rule",
                #"src/c++/src/capnp/CMakeLists.txt",
                ##"src/c++/src/capnp/common-test.cpp",
                #"src/c++/src/capnp/common.h",
                #"src/c++/src/capnp/compat",
                ##"src/c++/src/capnp/compat/json-test.cpp",
                #"src/c++/src/capnp/compat/json.cpp",
                #"src/c++/src/capnp/compat/json.capnp",
                #"src/c++/src/capnp/compat/json.capnp.cpp",
                #"src/c++/src/capnp/compat/json.capnp.h",
                #"src/c++/src/capnp/compat/json.h",
               #
                #"src/c++/src/capnp/dynamic-capability.cpp",
                ##"src/c++/src/capnp/dynamic-test.cpp",
                #"src/c++/src/capnp/dynamic.cpp",
                #"src/c++/src/capnp/dynamic.h",
                ##"src/c++/src/capnp/encoding-test.cpp",
                ##"src/c++/src/capnp/endian-fallback-test.cpp",
                #"src/c++/src/capnp/endian-reverse-test.cpp",
                ##"src/c++/src/capnp/endian-test.cpp",
                #"src/c++/src/capnp/endian.h",
                ##"src/c++/src/capnp/ez-rpc-test.cpp",
                #"src/c++/src/capnp/ez-rpc.cpp",
                #"src/c++/src/capnp/ez-rpc.h",
                ##"src/c++/src/capnp/fuzz-test.cpp",
                #"src/c++/src/capnp/generated-header-support.h",
                ##"src/c++/src/capnp/layout-test.cpp",
                #"src/c++/src/capnp/layout.cpp",
                #"src/c++/src/capnp/layout.h",
                #"src/c++/src/capnp/list.cpp",
                #"src/c++/src/capnp/list.h",
                ##"src/c++/src/capnp/membrane-test.cpp",
                #"src/c++/src/capnp/membrane.cpp",
                #"src/c++/src/capnp/membrane.h",
                ##"src/c++/src/capnp/message-test.cpp",
                #"src/c++/src/capnp/message.cpp",
                #"src/c++/src/capnp/message.h",
                ##"src/c++/src/capnp/orphan-test.cpp",
                #"src/c++/src/capnp/orphan.h",
                #"src/c++/src/capnp/persistent.capnp",
                #"src/c++/src/capnp/persistent.capnp.cpp",
                #"src/c++/src/capnp/persistent.capnp.h",
                #"src/c++/src/capnp/pointer-helpers.h",
                #"src/c++/src/capnp/pretty-print.h",
                #"src/c++/src/capnp/raw-schema.h",
                #"src/c++/src/capnp/rpc-prelude.h",
                ##"src/c++/src/capnp/rpc-test.cpp",
                ##"src/c++/src/capnp/rpc-twoparty-test.cpp",
                #"src/c++/src/capnp/rpc-twoparty.cpp",
                #"src/c++/src/capnp/rpc-twoparty.capnp",
                #"src/c++/src/capnp/rpc-twoparty.capnp.cpp",
                #"src/c++/src/capnp/rpc-twoparty.capnp.h",
                #"src/c++/src/capnp/rpc-twoparty.h",
                #"src/c++/src/capnp/rpc.cpp",
                #"src/c++/src/capnp/rpc.capnp",
                #"src/c++/src/capnp/rpc.capnp.cpp",
                #"src/c++/src/capnp/rpc.capnp.h",
                #"src/c++/src/capnp/rpc.h",
                #"src/c++/src/capnp/schema-lite.h",
                ##"src/c++/src/capnp/schema-loader-test.cpp",
                #"src/c++/src/capnp/schema-loader.cpp",
                #"src/c++/src/capnp/schema-loader.h",
                ##"src/c++/src/capnp/schema-parser-test.cpp",
                #"src/c++/src/capnp/schema-parser.cpp",
                #"src/c++/src/capnp/schema-parser.h",
                ##"src/c++/src/capnp/schema-test.cpp",
                #"src/c++/src/capnp/schema.cpp",
                #"src/c++/src/capnp/schema.capnp",
                #"src/c++/src/capnp/schema.capnp.cpp",
                #"src/c++/src/capnp/schema.capnp.h",
                #"src/c++/src/capnp/schema.h",
                ##"src/c++/src/capnp/serialize-async-test.cpp",
                #"src/c++/src/capnp/serialize-async.cpp",
                #"src/c++/src/capnp/serialize-async.h",
                ##"src/c++/src/capnp/serialize-packed-test.cpp",
                #"src/c++/src/capnp/serialize-packed.cpp",
                #"src/c++/src/capnp/serialize-packed.h",
                ##"src/c++/src/capnp/serialize-test.cpp",
                ##"src/c++/src/capnp/serialize-text-test.cpp",
                #"src/c++/src/capnp/serialize-text.cpp",
                #"src/c++/src/capnp/serialize-text.h",
                #"src/c++/src/capnp/serialize.cpp",
                #"src/c++/src/capnp/serialize.h",
                ##"src/c++/src/capnp/stringify-test.cpp",
                #"src/c++/src/capnp/stringify.cpp",
                #"src/c++/src/capnp/test-import.capnp",
                #"src/c++/src/capnp/test-import2.capnp",
                ##"src/c++/src/capnp/test-util.cpp",
                #"src/c++/src/capnp/test-util.h",
                #"src/c++/src/capnp/test.capnp",
                #"src/c++/src/capnp/testdata/errors.capnp.nobuild",
                #"src/c++/src/capnp/testdata/errors.txt",
                #"src/c++/src/capnp/testdata/lists.binary",
                #"src/c++/src/capnp/testdata/packedflat",
                #"src/c++/src/capnp/testdata/pretty.json",
                #"src/c++/src/capnp/testdata/pretty.txt",
                #"src/c++/src/capnp/testdata/segmented-packed",
                #"src/c++/src/capnp/testdata/short.json",
                #"src/c++/src/capnp/testdata/short.txt",
            ]
        },
        {
            "target_name":"capnp",
            'type':'executable',
            'defines':[	
            ],
            'include_dirs':[
                'config',
                "src\c++\src",
            ],
            'dependencies':[
                'capnp-compiler-dependencies',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
            },
            
            'sources':[
               "src/c++/src/capnp/compiler/capnp.cpp",
            ]
        },
        {
            "target_name":"capnpc-c++",
            'type':'executable',
            'defines':[	
            ],
            'include_dirs':[
                'config',
                "src\c++\src",
            ],
            'dependencies':[
                'capnp-compiler-dependencies',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
            },
            
            'sources':[
               "src/c++/src/capnp/compiler/capnpc-c++.cpp",
            ]
        },
        {
            "target_name":"capnpc-capnp",
            'type':'executable',
            'defines':[	
            ],
            'include_dirs':[
                'config',
                "src\c++\src",
            ],
            'dependencies':[
                'capnp-compiler-dependencies',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                ],
            },
            
            'sources':[
               "src/c++/src/capnp/compiler/capnpc-capnp.cpp",
            ]
        },
        {
            "target_name":"libcapnp",
            'type':'<(library)',
            'defines':[	
            ],
            'include_dirs':[
                'config',
                "src\c++\src",
            ],
            'dependencies':[
                #'copy_non_standard_extensions'
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    "src\c++\src",
                ],
            },
            
            'sources':[
                #"src/c++/src/capnp/afl-testcase.cpp",
                #"src/c++/src/capnp/any-test.cpp",
                "src/c++/src/capnp/any.cpp",
                "src/c++/src/capnp/any.h",
                "src/c++/src/capnp/arena.cpp",
                "src/c++/src/capnp/arena.h",
                #"src/c++/src/capnp/blob-test.cpp",
                "src/c++/src/capnp/blob.cpp",
                "src/c++/src/capnp/blob.h",

                "src/c++/src/capnp/c++.capnp",
                "src/c++/src/capnp/c++.capnp.cpp",
                "src/c++/src/capnp/c++.capnp.h",
                #"src/c++/src/capnp/canonicalize-test.cpp",
                #"src/c++/src/capnp/capability-test.cpp",
                "src/c++/src/capnp/capability.cpp",
                "src/c++/src/capnp/capability.h",
                "src/c++/src/capnp/CMakeLists.txt",
                #"src/c++/src/capnp/common-test.cpp",
                "src/c++/src/capnp/common.h",
                "src/c++/src/capnp/compat",
                #"src/c++/src/capnp/compat/json-test.cpp",
                "src/c++/src/capnp/compat/json.cpp",
                "src/c++/src/capnp/compat/json.capnp",
                "src/c++/src/capnp/compat/json.capnp.cpp",
                "src/c++/src/capnp/compat/json.capnp.h",
                "src/c++/src/capnp/compat/json.h",
               
                "src/c++/src/capnp/dynamic-capability.cpp",
                #"src/c++/src/capnp/dynamic-test.cpp",
                "src/c++/src/capnp/dynamic.cpp",
                "src/c++/src/capnp/dynamic.h",
                #"src/c++/src/capnp/encoding-test.cpp",
                #"src/c++/src/capnp/endian-fallback-test.cpp",
                #"src/c++/src/capnp/endian-reverse-test.cpp",
                #"src/c++/src/capnp/endian-test.cpp",
                "src/c++/src/capnp/endian.h",
                #"src/c++/src/capnp/ez-rpc-test.cpp",
                "src/c++/src/capnp/ez-rpc.cpp",
                "src/c++/src/capnp/ez-rpc.h",
                #"src/c++/src/capnp/fuzz-test.cpp",
                "src/c++/src/capnp/generated-header-support.h",
                #"src/c++/src/capnp/layout-test.cpp",
                "src/c++/src/capnp/layout.cpp",
                "src/c++/src/capnp/layout.h",
                "src/c++/src/capnp/list.cpp",
                "src/c++/src/capnp/list.h",
                #"src/c++/src/capnp/membrane-test.cpp",
                "src/c++/src/capnp/membrane.cpp",
                "src/c++/src/capnp/membrane.h",
                #"src/c++/src/capnp/message-test.cpp",
                "src/c++/src/capnp/message.cpp",
                "src/c++/src/capnp/message.h",
                #"src/c++/src/capnp/orphan-test.cpp",
                "src/c++/src/capnp/orphan.h",
                "src/c++/src/capnp/persistent.capnp",
                "src/c++/src/capnp/persistent.capnp.cpp",
                "src/c++/src/capnp/persistent.capnp.h",
                "src/c++/src/capnp/pointer-helpers.h",
                "src/c++/src/capnp/pretty-print.h",
                "src/c++/src/capnp/raw-schema.h",
                "src/c++/src/capnp/rpc-prelude.h",
                #"src/c++/src/capnp/rpc-test.cpp",
                #"src/c++/src/capnp/rpc-twoparty-test.cpp",
                "src/c++/src/capnp/rpc-twoparty.cpp",
                "src/c++/src/capnp/rpc-twoparty.capnp",
                "src/c++/src/capnp/rpc-twoparty.capnp.cpp",
                "src/c++/src/capnp/rpc-twoparty.capnp.h",
                "src/c++/src/capnp/rpc-twoparty.h",
                "src/c++/src/capnp/rpc.cpp",
                "src/c++/src/capnp/rpc.capnp",
                "src/c++/src/capnp/rpc.capnp.cpp",
                "src/c++/src/capnp/rpc.capnp.h",
                "src/c++/src/capnp/rpc.h",
                "src/c++/src/capnp/schema-lite.h",
                #"src/c++/src/capnp/schema-loader-test.cpp",
                "src/c++/src/capnp/schema-loader.cpp",
                "src/c++/src/capnp/schema-loader.h",
                #"src/c++/src/capnp/schema-parser-test.cpp",
                "src/c++/src/capnp/schema-parser.cpp",
                "src/c++/src/capnp/schema-parser.h",
                #"src/c++/src/capnp/schema-test.cpp",
                "src/c++/src/capnp/schema.cpp",
                "src/c++/src/capnp/schema.capnp",
                "src/c++/src/capnp/schema.capnp.cpp",
                "src/c++/src/capnp/schema.capnp.h",
                "src/c++/src/capnp/schema.h",
                #"src/c++/src/capnp/serialize-async-test.cpp",
                "src/c++/src/capnp/serialize-async.cpp",
                "src/c++/src/capnp/serialize-async.h",
                #"src/c++/src/capnp/serialize-packed-test.cpp",
                "src/c++/src/capnp/serialize-packed.cpp",
                "src/c++/src/capnp/serialize-packed.h",
                #"src/c++/src/capnp/serialize-test.cpp",
                #"src/c++/src/capnp/serialize-text-test.cpp",
                "src/c++/src/capnp/serialize-text.cpp",
                "src/c++/src/capnp/serialize-text.h",
                "src/c++/src/capnp/serialize.cpp",
                "src/c++/src/capnp/serialize.h",
                #"src/c++/src/capnp/stringify-test.cpp",
                "src/c++/src/capnp/stringify.cpp",
                #"src/c++/src/capnp/test-import.capnp",
                #"src/c++/src/capnp/test-import2.capnp",
                #"src/c++/src/capnp/test-util.cpp",
                #"src/c++/src/capnp/test-util.h",
                #"src/c++/src/capnp/test.capnp",
                #"src/c++/src/capnp/testdata",
                #"src/c++/src/capnp/testdata/binary",
                #"src/c++/src/capnp/testdata/errors.capnp.nobuild",
                #"src/c++/src/capnp/testdata/errors.txt",
                #"src/c++/src/capnp/testdata/flat",
                #"src/c++/src/capnp/testdata/lists.binary",
                #"src/c++/src/capnp/testdata/packed",
                #"src/c++/src/capnp/testdata/packedflat",
                #"src/c++/src/capnp/testdata/pretty.json",
                #"src/c++/src/capnp/testdata/pretty.txt",
                #"src/c++/src/capnp/testdata/segmented",
                #"src/c++/src/capnp/testdata/segmented-packed",
                #"src/c++/src/capnp/testdata/short.json",
                #"src/c++/src/capnp/testdata/short.txt",
            ]
        },
        {
            "target_name":"samples",
            'type':'none',
            'defines':[	
            ],
            'include_dirs':[
                'config',
                "src\c++\src",
            ],
            'dependencies':[
                #'copy_non_standard_extensions'
            ],
            'direct_dependent_settings': {
                'include_dirs': [

                ],
            },
            
            'sources':[
                "capnproto.gyp",
                "src/.travis.yml",
                "src/appveyor.yml",
                "src/c++/LICENSE.txt",
                "src/c++/README.txt",
                "src/c++/samples/addressbook.cpp",
                "src/c++/samples/addressbook.capnp",
                "src/c++/samples/calculator-client.cpp",
                "src/c++/samples/calculator-server.cpp",
                "src/c++/samples/calculator.capnp",
                "src/c++/samples/CMakeLists.txt",
                "src/c++/src/benchmark/capnproto-carsales.cpp",
                "src/c++/src/benchmark/capnproto-catrank.cpp",
                "src/c++/src/benchmark/capnproto-common.h",
                "src/c++/src/benchmark/capnproto-eval.cpp",
                "src/c++/src/benchmark/carsales.capnp",
                "src/c++/src/benchmark/carsales.proto",
                "src/c++/src/benchmark/catrank.capnp",
                "src/c++/src/benchmark/catrank.proto",
                "src/c++/src/benchmark/common.h",
                "src/c++/src/benchmark/eval.capnp",
                "src/c++/src/benchmark/eval.proto",
                "src/c++/src/benchmark/null-carsales.cpp",
                "src/c++/src/benchmark/null-catrank.cpp",
                "src/c++/src/benchmark/null-common.h",
                "src/c++/src/benchmark/null-eval.cpp",
                "src/c++/src/benchmark/protobuf-carsales.cpp",
                "src/c++/src/benchmark/protobuf-catrank.cpp",
                "src/c++/src/benchmark/protobuf-common.h",
                "src/c++/src/benchmark/protobuf-eval.cpp",
                "src/c++/src/benchmark/runner.cpp",
                "src/CONTRIBUTORS",
                "src/LICENSE",
            ]
        }

    ]
}