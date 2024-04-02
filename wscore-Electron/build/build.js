const { build } = require("electron-builder");

async function run() {
  try {
    await build({
      targets: build.Platform.WINDOWS.createTarget(),
      config: {
        directories: {
          output: "./dist/app",
        },
      },
    });
    console.log("Build completed successfully!");
  } catch (error) {
    console.error("Error occurred during build:", error);
  }
}

run();
