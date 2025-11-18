<!-- Quick Reference: Using Animations in Your Templates -->

# Animation Classes Quick Reference

## 🎨 Fade & Slide Animations

```html
<!-- Fade in with vertical movement -->
<div class="fade-in">This fades in smoothly</div>

<!-- Slide in from left -->
<div class="slide-in-left">Slides in from left</div>

<!-- Slide in from right -->
<div class="slide-in-right">Slides in from right</div>

<!-- Bounce animation -->
<div class="bounce">Bouncing element</div>

<!-- Glowing text effect -->
<h1 class="glow">Glowing Heading</h1>

<!-- Floating animation -->
<div class="floating">Floating element</div>
```

## 🎯 Card Animations

All `.card` elements automatically get:
- 3D hover effects
- Gradient top border on hover
- Lift animation on hover
- Smooth shadow transitions

```html
<!-- Standard card with auto-animations -->
<div class="card">
    <div class="card-body">
        <h5 class="card-title">Auto-Animated Card</h5>
        <p>Hover to see 3D effect</p>
    </div>
</div>

<!-- Job card with special styling -->
<div class="card job-card">
    <div class="job-type-badge">Full-time</div>
    <!-- Includes pulse animation -->
</div>

<!-- Dashboard card -->
<div class="dashboard-card">
    <div class="card-header">Dashboard</div>
    <div class="card-body">Content</div>
</div>
```

## 🔘 Button Animations

All `.btn` elements feature:
- Ripple effect on click
- Hover lift animation
- Smooth color transitions
- Scale effects

```html
<!-- Primary button with ripple -->
<button class="btn btn-primary">Click for Ripple</button>

<!-- Success button -->
<button class="btn btn-success">Success Action</button>

<!-- Danger button -->
<button class="btn btn-danger">Delete</button>
```

## 📊 Badge Animations

```html
<!-- Status badges with color-coded animations -->
<span class="status-badge status-pending">Pending</span>
<span class="status-badge status-reviewing">Reviewing</span>
<span class="status-badge status-accepted">Accepted</span>
<span class="status-badge status-rejected">Rejected</span>

<!-- Job type badges with pulse -->
<span class="job-type-badge">Full-time</span>
<span class="job-type-badge">Part-time</span>
```

## 🔔 Alert Animations

Auto-dismisses after 5 seconds with smooth fade-out:

```html
<!-- Success alert -->
<div class="alert alert-success">
    Success! Your action completed.
</div>

<!-- Error alert -->
<div class="alert alert-danger">
    Error! Something went wrong.
</div>

<!-- Warning alert -->
<div class="alert alert-warning">
    Warning! Please review.
</div>

<!-- Info alert -->
<div class="alert alert-info">
    Information message.
</div>
```

## 📝 Form Animations

```html
<div class="form-group">
    <label>Email Address</label>
    <input type="email" class="form-control" placeholder="Enter email">
    <!-- Auto-animates on focus with lift effect -->
</div>

<div class="search-bar">
    <!-- Slides up on page load -->
    <input type="text" class="form-control" placeholder="Search...">
</div>
```

## 🖼️ Company & Profile Elements

```html
<!-- Company logo with 3D rotation -->
<img src="logo.png" class="company-logo" alt="Company">

<!-- Profile image with floating animation -->
<img src="profile.jpg" class="profile-image" alt="Profile">

<!-- Profile header with gradient and glow -->
<div class="profile-header">
    <h1>User Profile</h1>
</div>
```

## 🚀 JavaScript Functions

### Show Notifications
```javascript
// Success notification (auto-closes after 4s)
notify('Action completed successfully!', 'success');

// Error notification
notify('An error occurred!', 'error');

// Warning notification
notify('Please be careful!', 'warning');

// Info notification
notify('FYI: Something happened', 'info');

// Custom duration
notify('Message', 'success', 2000); // 2 seconds
```

### Animate Counters
```javascript
// Animate number from 0 to target
animateCounter($('.counter'), 100, 2000);
// Counts to 100 over 2 seconds

// In HTML:
<div class="counter" data-target="100">0</div>
```

### Smooth Scroll
```html
<!-- Click to scroll smoothly to section -->
<a href="#features">Scroll to Features</a>

<section id="features">
    Features section...
</section>
```

## 🎬 Advanced: Custom Animations

### Create custom animation
```css
@keyframes myCustomAnimation {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    50% {
        opacity: 0.5;
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

.my-element {
    animation: myCustomAnimation 1s ease-out;
}
```

### 3D Transform Example
```html
<div class="my-3d-box">
    <style>
        .my-3d-box {
            perspective: 1000px;
            width: 200px;
            height: 200px;
            transition: transform 0.6s;
        }
        
        .my-3d-box:hover {
            transform: rotateX(10deg) rotateY(10deg) rotateZ(5deg);
        }
    </style>
</div>
```

## 🔧 How to Apply Animations

### Method 1: Using CSS Classes
```html
<!-- Apply animation class directly -->
<div class="fade-in">Content fades in</div>
<div class="slide-in-left">Slides in from left</div>
```

### Method 2: Using Element Type
```html
<!-- All cards get 3D hover automatically -->
<div class="card">Auto-animated</div>

<!-- All buttons get ripple effect -->
<button class="btn btn-primary">Animated button</button>
```

### Method 3: jQuery/JavaScript
```javascript
// Apply fade-in animation programmatically
$('#my-element').addClass('fade-in');

// Trigger notification
notify('Custom message', 'success');

// Custom animation
$('#element').animate({ opacity: 0.5 }, 1000);
```

## 📱 Mobile Optimizations

Animations automatically optimize for mobile:
- Shorter durations on mobile
- Reduced 3D complexity
- Touch-optimized interactions
- Accessible animations

## ⚙️ Configuration

### Disable animations for users who prefer reduced motion
```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
```

### Change animation colors globally
Edit `static/css/animations-3d.css` and change color values:
```css
/* Primary color for animations */
background: linear-gradient(90deg, #YOUR_COLOR1, #YOUR_COLOR2);
```

## 🎯 Best Practices

1. **Use semantic HTML** - Let CSS handle the animations
2. **Mobile-first** - Test animations on mobile first
3. **Performance** - Use `transform` and `opacity` for smooth animations
4. **Accessibility** - Respect `prefers-reduced-motion`
5. **User Experience** - Don't overuse animations
6. **Loading** - Keep animation files lightweight

## 🐛 Debugging Animations

### Check if animations are loading
```javascript
// In browser console
var sheet = document.styleSheets;
console.log('CSS files loaded:', sheet.length);

// Check for JavaScript errors
console.error() // Shows any errors
```

### Test animation performance
1. Open DevTools (F12)
2. Go to Performance tab
3. Start recording
4. Trigger animation
5. Stop and analyze FPS

## 📚 Complete Animation List

| Class/Element | Animation | Duration | Trigger |
|---|---|---|---|
| `.fade-in` | Fade with slide | 0.5s | On load |
| `.slide-in-left` | Slide from left | 0.6s | On load/scroll |
| `.slide-in-right` | Slide from right | 0.6s | On load/scroll |
| `.card` | 3D hover | 0.4s | On hover |
| `.btn` | Ripple + lift | 0.3s-0.6s | On click/hover |
| `.alert` | Slide down fade | 0.4s | Auto-dismiss 5s |
| `.job-type-badge` | Pulse | 2s | Continuous |
| `.profile-image` | Float | 3s | Continuous |
| `.jumbotron` | Gradient shift | 15s | Continuous |

---

**Pro Tip**: Combine multiple classes for complex animations:
```html
<div class="card fade-in">Double animated!</div>
```

**Remember**: Great animations enhance UX, but excessive animations hurt performance!
