add_plugin(logPolarMinimalPathTracer)

target_sources(logPolarMinimalPathTracer PRIVATE
    logPolarMinimalPathTracer.cpp
    logPolarMinimalPathTracer.h
    logPolarMinimalPathTracer.rt.slang
)
target_copy_shaders(logPolarMinimalPathTracer RenderPasses/logPolarMinimalPathTracer)

target_source_group(logPolarMinimalPathTracer "RenderPasses")
