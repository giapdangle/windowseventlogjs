{
  'targets': [
    {
      'target_name': 'EventLog',
      'conditions': [
          ['OS=="win"', {
            'msvs_settings': {
              'VCCLCompilerTool': {                  
                'RuntimeTypeInfo':'true',
                'RuntimeLibrary':'MultiThreadedDLL'
              }
            },
            'msbuild_settings': {
              'ClCompile': {
                'ExceptionHandling': 'Async',
                'CompileAsManaged':'true'
              }
            }
          }]
      ],
      'include_dirs': ['.'],
      'sources': [
        'src/EventLog.cpp'
      ]
    }
  ]
}