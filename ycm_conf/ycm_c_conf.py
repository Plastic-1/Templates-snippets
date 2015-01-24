import os
import sys
import ycm_core

if sys.platform.startswith('linux'):
    flags = [
    '-Wall','-Wextra','-Werror',
    '-Wno-long-long','-Wno-variadic-macros','-fexceptions',
    '-DNDEBUG','-DUSE_CLANG_COMPLETER',
    '-std=c99',
    '-x','c',
    '-I','.',
    '-I','./ClangCompleter',
    '-isystem','/usr/include/',
    '-isystem','/usr/include/bsd/'
    ]
elif sys.platform.startswith('darwin'):
    flags = [
    '-Wall','-Wextra','-Werror',
    '-Wno-long-long', '-Wno-variadic-macros', '-fexceptions',
    '-DNDEBUG', '-DUSE_CLANG_COMPLETER',
    '-std=c99',
    '-x','c',
    '-isystem', '/System/Library/Frameworks/Python.framework/Headers',
    '-isystem', '../llvm/include',
    '-isystem', '../llvm/tools/clang/include',
    '-I', '.',
    '-I', './ClangCompleter',
    '-isystem', './tests/gmock/gtest',
    '-isystem', './tests/gmock/gtest/include',
    '-isystem', './tests/gmock',
    '-isystem', './tests/gmock/include',
    '-isystem', '/usr/include',
    '-isystem', '/usr/local/include',
    '-isystem', '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include',
    ]
    
compilation_database_folder = ''

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
else:
  database = None


def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def FlagsForFile( filename ):
  if database:
    compilation_info = database.GetCompilationInfoForFile( filename )
    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )
  else:
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }
