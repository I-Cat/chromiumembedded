# Copyright (c) 2011 The Chromium Embedded Framework Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'includes': [
    # Bring in the autogenerated source file lists.
    'cef_paths.gypi',
   ],
  'variables': {
    'includes_common': [
      'include/base/cef_atomic_ref_count.h',
      'include/base/cef_atomicops.h',
      'include/base/cef_basictypes.h',
      'include/base/cef_bind.h',
      'include/base/cef_bind_helpers.h',
      'include/base/cef_build.h',
      'include/base/cef_callback.h',
      'include/base/cef_callback_forward.h',
      'include/base/cef_callback_helpers.h',
      'include/base/cef_callback_list.h',
      'include/base/cef_cancelable_callback.h',
      'include/base/cef_lock.h',
      'include/base/cef_logging.h',
      'include/base/cef_macros.h',
      'include/base/cef_move.h',
      'include/base/cef_platform_thread.h',
      'include/base/cef_ref_counted.h',
      'include/base/cef_scoped_ptr.h',
      'include/base/cef_string16.h',
      'include/base/cef_template_util.h',
      'include/base/cef_thread_checker.h',
      'include/base/cef_thread_collision_warner.h',
      'include/base/cef_trace_event.h',
      'include/base/cef_tuple.h',
      'include/base/cef_weak_ptr.h',
      'include/base/internal/cef_bind_internal.h',
      'include/base/internal/cef_callback_internal.h',
      'include/base/internal/cef_lock_impl.h',
      'include/base/internal/cef_raw_scoped_refptr_mismatch_checker.h',
      'include/base/internal/cef_thread_checker_impl.h',
      'include/cef_base.h',
      'include/cef_pack_resources.h',
      'include/cef_pack_strings.h',
      'include/cef_runnable.h',
      'include/cef_version.h',
      'include/internal/cef_export.h',
      'include/internal/cef_logging_internal.h',
      'include/internal/cef_ptr.h',
      'include/internal/cef_string.h',
      'include/internal/cef_string_list.h',
      'include/internal/cef_string_map.h',
      'include/internal/cef_string_multimap.h',
      'include/internal/cef_string_types.h',
      'include/internal/cef_string_wrappers.h',
      'include/internal/cef_thread_internal.h',
      'include/internal/cef_time.h',
      'include/internal/cef_trace_event_internal.h',
      'include/internal/cef_types.h',
      'include/internal/cef_types_wrappers.h',
      '<@(autogen_cpp_includes)',
    ],
    'includes_capi': [
      'include/capi/cef_base_capi.h',
      '<@(autogen_capi_includes)',
    ],
    'includes_wrapper': [
      'include/wrapper/cef_byte_read_handler.h',
      'include/wrapper/cef_closure_task.h',
      'include/wrapper/cef_helpers.h',
      'include/wrapper/cef_message_router.h',
      'include/wrapper/cef_stream_resource_handler.h',
      'include/wrapper/cef_xml_object.h',
      'include/wrapper/cef_zip_archive.h',
    ],
    'includes_win': [
      'include/base/internal/cef_atomicops_x86_msvc.h',
      'include/base/internal/cef_bind_internal_win.h',
      'include/cef_sandbox_win.h',
      'include/internal/cef_types_win.h',
      'include/internal/cef_win.h',
    ],
    'includes_mac': [
      'include/base/internal/cef_atomicops_atomicword_compat.h',
      'include/base/internal/cef_atomicops_mac.h',
      'include/cef_application_mac.h',
      'include/internal/cef_mac.h',
      'include/internal/cef_types_mac.h',
    ],
    'includes_linux': [
      'include/base/internal/cef_atomicops_atomicword_compat.h',
      'include/base/internal/cef_atomicops.h',
      'include/internal/cef_linux.h',
      'include/internal/cef_types_linux.h',
    ],
    'libcef_sources_common': [
      'libcef_dll/cpptoc/cpptoc.h',
      'libcef_dll/ctocpp/ctocpp.h',
      'libcef_dll/libcef_dll.cc',
      'libcef_dll/libcef_dll2.cc',
      'libcef_dll/resource.h',
      'libcef_dll/transfer_util.cpp',
      'libcef_dll/transfer_util.h',
      '<@(autogen_library_side)',
    ],
    'libcef_dll_wrapper_sources_common': [
      'libcef_dll/base/cef_bind_helpers.cc',
      'libcef_dll/base/cef_callback_helpers.cc',
      'libcef_dll/base/cef_callback_internal.cc',
      'libcef_dll/base/cef_lock.cc',
      'libcef_dll/base/cef_lock_impl.cc',
      'libcef_dll/base/cef_logging.cc',
      'libcef_dll/base/cef_ref_counted.cc',
      'libcef_dll/base/cef_string16.cc',
      'libcef_dll/base/cef_thread_checker_impl.cc',
      'libcef_dll/base/cef_thread_collision_warner.cc',
      'libcef_dll/base/cef_weak_ptr.cc',
      'libcef_dll/cpptoc/base_cpptoc.h',
      'libcef_dll/cpptoc/cpptoc.h',
      'libcef_dll/ctocpp/base_ctocpp.h',
      'libcef_dll/ctocpp/ctocpp.h',
      'libcef_dll/transfer_util.cpp',
      'libcef_dll/transfer_util.h',
      'libcef_dll/wrapper/cef_browser_info_map.h',
      'libcef_dll/wrapper/cef_byte_read_handler.cc',
      'libcef_dll/wrapper/cef_closure_task.cc',
      'libcef_dll/wrapper/cef_message_router.cc',
      'libcef_dll/wrapper/cef_stream_resource_handler.cc',
      'libcef_dll/wrapper/cef_xml_object.cc',
      'libcef_dll/wrapper/cef_zip_archive.cc',
      'libcef_dll/wrapper/libcef_dll_wrapper.cc',
      'libcef_dll/wrapper/libcef_dll_wrapper2.cc',
      '<@(autogen_client_side)',
    ],
    'cefclient_bundle_resources_common': [
      'tests/cefclient/res/binding.html',
      'tests/cefclient/res/dialogs.html',
      'tests/cefclient/res/domaccess.html',
      'tests/cefclient/res/localstorage.html',
      'tests/cefclient/res/logo.png',
      'tests/cefclient/res/osr_test.html',
      'tests/cefclient/res/other_tests.html',
      'tests/cefclient/res/performance.html',
      'tests/cefclient/res/performance2.html',
      'tests/cefclient/res/transparency.html',
      'tests/cefclient/res/window.html',
      'tests/cefclient/res/xmlhttprequest.html',
    ],
    'cefclient_sources_common': [
      'tests/cefclient/cefclient.cpp',
      'tests/cefclient/cefclient.h',
      'tests/cefclient/binding_test.cpp',
      'tests/cefclient/binding_test.h',
      'tests/cefclient/bytes_write_handler.cpp',
      'tests/cefclient/bytes_write_handler.h',
      'tests/cefclient/client_app.cpp',
      'tests/cefclient/client_app.h',
      'tests/cefclient/client_app_delegates.cpp',
      'tests/cefclient/client_handler.cpp',
      'tests/cefclient/client_handler.h',
      'tests/cefclient/client_renderer.cpp',
      'tests/cefclient/client_renderer.h',
      'tests/cefclient/client_switches.cpp',
      'tests/cefclient/client_switches.h',
      'tests/cefclient/dialog_test.cpp',
      'tests/cefclient/dialog_test.h',
      'tests/cefclient/dom_test.cpp',
      'tests/cefclient/dom_test.h',
      'tests/cefclient/dragdrop_events.h',
      'tests/cefclient/osrenderer.h',
      'tests/cefclient/osrenderer.cpp',
      'tests/cefclient/performance_test.cpp',
      'tests/cefclient/performance_test.h',
      'tests/cefclient/performance_test_setup.h',
      'tests/cefclient/performance_test_tests.cpp',
      'tests/cefclient/resource_util.h',
      'tests/cefclient/scheme_test.cpp',
      'tests/cefclient/scheme_test.h',
      'tests/cefclient/string_util.cpp',
      'tests/cefclient/string_util.h',
      'tests/cefclient/window_test.cpp',
      'tests/cefclient/window_test.h',
      '<@(cefclient_bundle_resources_common)',
    ],
    'cefclient_sources_win': [
      'tests/cefclient/cefclient.exe.manifest',
      'tests/cefclient/cefclient.rc',
      'tests/cefclient/cefclient_osr_dragdrop_win.h',
      'tests/cefclient/cefclient_osr_dragdrop_win.cpp',
      'tests/cefclient/cefclient_osr_widget_win.h',
      'tests/cefclient/cefclient_osr_widget_win.cpp',
      'tests/cefclient/cefclient_win.cpp',
      'tests/cefclient/client_handler_win.cpp',
      'tests/cefclient/resource.h',
      'tests/cefclient/res/cefclient.ico',
      'tests/cefclient/res/small.ico',
      'tests/cefclient/resource_util_win.cpp',
      'tests/cefclient/window_test_win.cpp',
    ],
    'cefclient_sources_mac': [
      'tests/cefclient/cefclient_mac.mm',
      'tests/cefclient/cefclient_osr_widget_mac.h',
      'tests/cefclient/cefclient_osr_widget_mac.mm',
      'tests/cefclient/client_handler_mac.mm',
      'tests/cefclient/resource_util_mac.mm',
      'tests/cefclient/resource_util_posix.cpp',
      'tests/cefclient/window_test_mac.mm',
    ],
    'cefclient_sources_mac_helper': [
      'tests/cefclient/binding_test.cpp',
      'tests/cefclient/binding_test.h',
      'tests/cefclient/client_app.cpp',
      'tests/cefclient/client_app.h',
      'tests/cefclient/client_app_delegates.cpp',
      'tests/cefclient/client_handler.cpp',
      'tests/cefclient/client_handler.h',
      'tests/cefclient/client_handler_mac.mm',
      'tests/cefclient/client_renderer.cpp',
      'tests/cefclient/client_renderer.h',
      'tests/cefclient/client_switches.cpp',
      'tests/cefclient/client_switches.h',
      'tests/cefclient/dialog_test.cpp',
      'tests/cefclient/dialog_test.h',
      'tests/cefclient/dom_test.cpp',
      'tests/cefclient/dom_test.h',
      'tests/cefclient/performance_test.cpp',
      'tests/cefclient/performance_test.h',
      'tests/cefclient/performance_test_setup.h',
      'tests/cefclient/performance_test_tests.cpp',
      'tests/cefclient/process_helper_mac.cpp',
      'tests/cefclient/resource_util.h',
      'tests/cefclient/resource_util_mac.mm',
      'tests/cefclient/resource_util_posix.cpp',
      'tests/cefclient/scheme_test.cpp',
      'tests/cefclient/scheme_test.h',
      'tests/cefclient/string_util.cpp',
      'tests/cefclient/string_util.h',
      'tests/cefclient/window_test.cpp',
      'tests/cefclient/window_test.h',
      'tests/cefclient/window_test_mac.mm',
    ],
    'cefclient_bundle_resources_mac': [
      'tests/cefclient/mac/cefclient.icns',
      'tests/cefclient/mac/English.lproj/InfoPlist.strings',
      'tests/cefclient/mac/English.lproj/MainMenu.xib',
      'tests/cefclient/mac/Info.plist',
      '<@(cefclient_bundle_resources_common)',
    ],
    'cefclient_sources_linux': [
      'tests/cefclient/cefclient_gtk.cpp',
      'tests/cefclient/cefclient_osr_widget_gtk.h',
      'tests/cefclient/cefclient_osr_widget_gtk.cpp',
      'tests/cefclient/client_handler_gtk.cpp',
      'tests/cefclient/print_handler_gtk.cpp',
      'tests/cefclient/print_handler_gtk.h',
      'tests/cefclient/resource_util_linux.cpp',
      'tests/cefclient/resource_util_posix.cpp',
      'tests/cefclient/window_test_gtk.cpp',
    ],
    'cefclient_bundle_resources_linux': [
      '<@(cefclient_bundle_resources_common)',
    ],
    'cefsimple_sources_common': [
      'tests/cefsimple/simple_app.cpp',
      'tests/cefsimple/simple_app.h',
      'tests/cefsimple/simple_handler.cpp',
      'tests/cefsimple/simple_handler.h',
    ],
    'cefsimple_sources_win': [
      'tests/cefsimple/cefsimple.exe.manifest',
      'tests/cefsimple/cefsimple.rc',
      'tests/cefsimple/cefsimple_win.cpp',
      'tests/cefsimple/simple_handler_win.cpp',
      'tests/cefsimple/resource.h',
      'tests/cefsimple/res/cefsimple.ico',
      'tests/cefsimple/res/small.ico',
    ],
    'cefsimple_sources_mac': [
      'tests/cefsimple/cefsimple_mac.mm',
      'tests/cefsimple/simple_handler_mac.mm',
    ],
    'cefsimple_sources_mac_helper': [
      'tests/cefsimple/process_helper_mac.cpp',
    ],
    'cefsimple_bundle_resources_mac': [
      'tests/cefsimple/mac/cefsimple.icns',
      'tests/cefsimple/mac/English.lproj/InfoPlist.strings',
      'tests/cefsimple/mac/English.lproj/MainMenu.xib',
      'tests/cefsimple/mac/Info.plist',
    ],
    'cefsimple_sources_linux': [
      'tests/cefsimple/cefsimple_linux.cpp',
      'tests/cefsimple/simple_handler_aura.cpp',
    ],
  },
}
