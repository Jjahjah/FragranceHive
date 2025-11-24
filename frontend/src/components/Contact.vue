<template>
  <div class="container mt-5">
    <h1 class="mb-4 text-primary">Contact Us</h1>
    <p>If you have any questions or feedback, feel free to reach out!</p>

    <form>
      <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" class="form-control" id="name" placeholder="Your name" />
      </div>

      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email" placeholder="you@example.com" />
      </div>

      <div class="mb-3">
        <label for="message" class="form-label">Message</label>
        <textarea class="form-control" id="message" rows="5" placeholder="Your message"></textarea>
      </div>

      <button type="submit" class="btn btn-primary">Send Message</button>
    </form>
  </div>
</template>

<script setup>
// No reactive logic yet, this is static for now
</script>

<style scoped>
/* Optional: add custom styles */
h1 {
  font-weight: bold;
}
</style>
